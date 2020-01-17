---
title: "How to Solve: Error fetching http headers"
description: "Error Fetching http headers is a common error to encounter when working with the SLAPI. Here is how to fix it."
date: "2013-03-19"
author: "phil"
tags:
    - "blog"
    - "article"
aliases :
    - "/blog/phil/how-solve-error-fetching-http-headers/"
---

`"Error Fetching http headers"` is a common error to encounter when working with the SLAPI. Fortunately, it is not terribly difficult to avoid. This error most commonly met when working with a large sets of data and can be a bit cryptic, as it seems to imply some sort of connection issue. In truth, it is a client side error provided when a timeout occurs while waiting for a response from the API.


When this error is encountered, there are three common solutions to head off the error by remedying either the timeout directly or how the API returns the results.

# The Problem

Lets say you want to get information about your account, so you make a API call to [SoftLayer_Account::getObject](/reference/services/SoftLayer_Account/getObject/), which works perfectly fine. Then you add an object mask to that API call to pull in various relational properties, like invoices, tickets, hardware etc. Which all works fine because your account is new and doesn't have many of those things on it. Time goes by, and slowly that API call starts taking a bit longer as each month you get increasingly more complex invoices, more tickets, hardware etc. Each time you make this API call, our database has to pull all of this information together before returning it to you, and eventually you'll get hit with this error, and wonder what went wrong. 

# The Solutions

There isn't really a hard limit on how many objects you can request in an API call, as it really just depends on how long it takes our database to get them all collected for you. However there are a few things you can try.

### Socket Timeout

This varies depending on what client you are using to communicate with the SLAPI, but increasing your timeout limit to several minutes may help. Re-trying the request itself might also work. This is the easiest solution, but also the least likely to work long term.


### [Object masks](/article/object-masks/)

In our problem example, lets say we are using the following object mask `mask[invoices, tickets, hardware]`, which will get our invoices, tickets, and hardware as you might expect. Since we have a great number of all of those, the API call returns `"Error Fetching http headers"`, so we can use our object mask to limit what we get back.

We can do this by adding in some `Local` properties to limit the amount of data returned. `mask[invoices[id], tickets[id], hardware[id]]` for example, will only return the `id` of each invoice, ticket, and hardware. When you select `Local` properties in an object mask, all other unspecified properties are UNselected in turn.

### Breaking up the API call

ALternatively, you can usually break up the API call into multiple parts. `SoftLayer_Account::getObject(objectMask=mask[invoices, tickets, hardware])` could be broken up into

- `SoftLayer_Account::getInvoices()`
- `SoftLayer_Account::getTickets()`
- `SoftLayer_Account::getHardware()`

Generally speaking, most relational properties on a service will have a corresponding `get` method. So `tickets` becomes `getTickets`.

### [Result limits](/article/using-result-limits-softlayer-api/)

The use of result limits allows for [pagination](https://en.wikipedia.org/wiki/Pagination) of the returned objects. By setting the number of objects to return and an offset to start from, batch processing of results is possible, which results in a quicker processing time overall.

The trick with result limits though is that the method you call has to return a list. [SoftLayer_Account::getObject](/reference/services/SoftLayer_Account/getObject/) for example only returns a single object, so you can not use a result limit there. However, methods like [SoftLayer_Account::getHardware](/reference/services/SoftLayer_Account/getHardware/) return a list, and you can use a result limit to step through the data and avoid the error.



-Phil

