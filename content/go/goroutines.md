---
title: "Goroutines, Pagination and the SoftLayer API"
description: "Describes some ways to implement concurrency in your golang applications when interacting with the SoftLayer API. A few examples and explanation of softlayer-go's features."
date: "2024-02-16"
tags:
    - "cli"
    - "sdk"
    - "pagination"
    - "resultlimit"
---

# Basics of Goroutines
If you are unfamiliar with Goroutines, they are a way to easily add paralleism to your application. For a brief explanation on how they work in go, check out the following:

- [What are goroutines and how are they scheduled?](https://dev.to/gophers/what-are-goroutines-and-how-are-they-scheduled-2nj3)
- [Understanding Golang and Goroutines](https://medium.com/technofunnel/understanding-golang-and-goroutines-72ac3c9a014d)
- [Goroutines Crash Course (Mutex, Channels, Wait Group, & More!)](https://www.youtube.com/watch?v=5Z8skvm4g64)
- [https://www.youtube.com/watch?v=Bk1c30avsuU](https://www.youtube.com/watch?v=Bk1c30avsuU)


The basic pattern here will be to make a single api call to get the first set of results, but also the expected total number of results. From there we will use goroutines to create a thread for each needed API call, wait for them all to finish and collect the results.

# Examples from the softlayer-go SDK

In [v1.1.4](https://github.com/softlayer/softlayer-go/releases/tag/v1.1.3) I've added a couple of helper functions that user goroutiunes to paginate through API results, and will likely add more in the future. For now I will use these as examples and go in detail about what these functions do, and how they do it.

## [The Code](https://github.com/softlayer/softlayer-go/blob/master/helpers/virtual/virtual.go#L167)


```go
func GetVirtualGuestsIter(session session.SLSession, options *sl.Options) (resp []datatypes.Virtual_Guest, err error) {

    options.SetOffset(0)
    limit := options.ValidateLimit()

    // Can't call service.GetVirtualGuests because it passes a copy of options, not the address to options sadly.
    err = session.DoRequest("SoftLayer_Account", "getVirtualGuests", nil, options, &resp)
    if err != nil {
        return
    }
    apicalls := options.GetRemainingAPICalls()
    var wg sync.WaitGroup
    for x := 1; x <= apicalls; x++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            offset := i * limit
            this_resp := []datatypes.Virtual_Guest{}
            options.Offset = &offset
            err = session.DoRequest("SoftLayer_Account", "getVirtualGuests", nil, options, &this_resp)
            if err != nil {
                fmt.Printf("[ERROR] %v\n", err)
            }
            resp = append(resp, this_resp...)
        }(x)
    }
    wg.Wait()
    return resp, err
}
```

This function takes in two arguments. The first is a copy of your session, and the second is a pointer to your request options, which will include any ObjectMask or ObjectFilter you set. You might also want to set a specific ResultLimit if the default of 50 isn't appropriate. This function will return a slice of Virtual_Guests and an error (if any). Error handling with goroutines can be a bit tricky, so for these examples I opted to just print the errors out. `err` will only not be nil if the first API call errors, or the last api call errors. Any errors between that will be somewhat lost. To improve on that, we would need to use a [sync/errorgroup](https://pkg.go.dev/golang.org/x/sync/errgroup).


```go
    options.SetOffset(0)
    limit := options.ValidateLimit()
```
This will force the Offset to be 0, and make sure the limit is set to something valid (>2 basically, a resultLimit of 1 will only return a single result, and go expects a slice of results, which will cause errors).

```go
    err = session.DoRequest("SoftLayer_Account", "getVirtualGuests", nil, options, &resp)
    if err != nil {
        return
    }
    apicalls := options.GetRemainingAPICalls()
```

Next we make a single API call to get the first set of results, along with finding out how many results we should expect (this is from the `SoftLayer-Total-Items` result header) 

> *NOTE* This will only work if you are using the `REST` endpoint, the XMLRPC endpoint isn't setup to save the results of the `SoftLayer-Total-Items` header currently. You can still use goroutines, but you will have to iterate through results until you get less results than your Limit, which isn't great if you don't know how many API calls you have to make.

```go
    var wg sync.WaitGroup
```

The `wg` is a WaitGroup, which basically lets go collect the results of all the API calls we made. 

> *NOTE* The order of the results might not reflect the order from the API since API calls will return in a somewhat random order. You may need to sort this slice after the API calls are completed.


```go
    for x := 1; x <= apicalls; x++ {
        wg.Add(1)
        ...
    }
```

Since we know how many API calls are needed, we will create a goroutine for each one, incrementing `wg` by 1. We could likely do `wg.Add(apicalls)` before the for loop, but this pattern matches a lot of what you will see in other examples so I kept it that way.


```go
go func(i int) {
    defer wg.Done()
    ...
}(x)
```

This will launch a goroutine (with the keyworkd `go` here) and pass in `i` (the iteration count) to the function. This lets us know what our offset needs to be for each API call, so were not getting the same data over and over again. Then we `defer` the closure of the `wg` waitgroup, which basically tells the waitgroup that this goroutine is done.

```go
    offset := i * limit
    this_resp := []datatypes.Virtual_Guest{}
    options.Offset = &offset
    err = session.DoRequest("SoftLayer_Account", "getVirtualGuests", nil, options, &this_resp)
    if err != nil {
        fmt.Printf("[ERROR] %v\n", err)
    }
    resp = append(resp, this_resp...)
```

From here we just make an API call. Increment the offset, create a holder for the result, set the offset, make the API call. Check for the error and print it out if any, then append the response to the main slice of responses.


The reason we have to call `session.DoRequest` directly is because calling the services.Account::GetVirtualGeusts() method will pass a copy of our options into the session, which means we don't get updated on the amount of SoftLayer-Total-Items we have to expect. A bit of a pain to deal with, but this final format isn't too bad to work with.

```go
    wg.Wait()
    return resp, err
```

Finally we wait for the `wg` Waitgroup to finish all its tasks, then just return the result and err.


# Notes
- This method of pagination will only work on the `REST` endpoint for now. If you need it to work on the `XMLRPC` endpoint feel free to [Open an issue](https://github.com/softlayer/softlayer-go/issues/new) to let me know there is demand for that.
- Any errors after the first will largely be ignored with this function, which isn't great. Generally the only errors you might hit assuming the first call worked would be a rate limit exception. Try to keep your requests to under 50/second and you should avoid this limit. I may add an auto limiter to this function one day, but for now just be aware of that.
- Always use a OrderBy ObjectFilter when using [resultlimits](https://sldn.softlayer.com/article/using-result-limits-softlayer-api/) to ensure each API call gets the same section of results. Without an OrderBy the database can sometimes use a different index between api calls causing some data overlap. HOWEVER, becuase the results of the goroutines might come back out of order, `resp` might not be ordered by what you specified in the ObjectFilter.