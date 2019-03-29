---
title: "REST"
description: "Getting started with REST API calls"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "resultlimit"
    - "objectmask"
---


SoftLayer provides a RESTful API in addition to RPC-style API services. Use the REST API in cases where your programming language may not have good SOAP or XML-RPC support but can perform simple HTTP protocol actions and can interpret XML or JSON data.


## REST URLs
REST API URLs are structured to easily traverse SoftLayer's object hierarchy. A basic REST request is structured as follows:

```
curl -u [username]:[apiKey]  -d '{"parameters": ["first", "second"]}'
https://api.[service.]softlayer.com/rest/v3.1/[serviceName]/[initializationParameter]/[methodName].[json|xml|txt]?
objectMask=mask[]&objectFilter={}&resultLimit=0,1
```

* All REST requests, even private network requests, must be passed through HTTP SSL.
* Use your API username and key to authenticate your request through HTTP authentication.
* The base hostname and folder name for a REST request is either `api.softlayer.com/rest/v3.1/` or `api.service.softlayer.com/rest/v3.1/`. 
* `api.service.softlayer.com` is used to access the API over the SoftLayer private network. It is also required to use this endpoint when using the [Resource_Metadata](https://softlayer.github.io/reference/services/SoftLayer_Resource_Metadata/) service.
* Follow up the base URL with the name of the API service you wish to call, for instance "SoftLayer_Account" or "SoftLayer_Hardware_Server".
* If your API request requires an initialization parameter then add a slash followed by your init parameter id to your URL.</li>
* The SoftLayer REST API can return either XML, JSON or TXT formatted output. Add ".xml", ".json", or ".txt" to the end of your request to specify which format you'd like to receive data in.

A request like this calls the getObject() method of the API service you're trying to call. [SoftLayer_Account::getObject](/reference/services/SoftLayer_Account/getObject) doesn't require an initialization parameter, so its REST URL looks like this

```
https://username:apiKey@api.softlayer.com/rest/v3/SoftLayer_Account.json
```

> To know if an API call requires initialization parameters, look for `<serviceName>InitParams` in the `required headers` section of the method's documentation

To call the [getObject()](/reference/services/SoftLayer_Hardware_Server/getObject) method for a specific [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server/) record use the following URL, assuming "1234" is the id of the server you wish to retrieve:

```
https://api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/1234.json
```

> By default, if you use a GET request, the SL API assumes you want the getObject() method. If you use POST, it assums createObject().


Call API methods other than `getObject()` by placing the method's name after your initialization parameter. 

### Rest Url Tricks

When building a REST API call, you can drill down into the various relational properites.

For example:

```
https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware
```

Will return a list of all hardware on a given account, via the [SoftLayer_Account::hardware](/reference/datatypes/SoftLayer_Account/#hardware) property.

If you wanted a specific hardware object, you could do

* `https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware/365112/`
> You could also do SoftLayer_Hardware_Server/35112/getObject of course. This format is more useful when you want to get a specific data bit that doens't have a corresponding service.

And you can go deeper, if you wanted to get just the hardwares [networkComponents](/reference/datatypes/SoftLayer_Hardware_SErver/#networkComponents) you can do this:

```
https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware/365112/getNetworkComponents
```

A specific network component?

```
https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware/365112/getNetworkComponents/22222
```

### Rest Versions

In the url, you will see `v3.1` or `v3`. Both versions are basically the same, `v3.1` is the "newer" version, and the only real difference is it handles objectFilters a little faster.

## HTTP Request Types
It is important to understand that the REST endpoint is mostly just a wrapper for the SOAP endpoint, and as such might not work exactly like other REST services.

As a general rule, you can use a `GET` request UNLESS you need to send in optional parameters, then you should use a `POST` request.

### DELETE
A `DELETE` request assume you want to use the `deleteObject()` method. 
```
curl -X DELETE https://api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234.json
```

> Using `curl -X GET https://api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234/deleteObject.json` will get you the same result

### GET
Use a `GET` request for method that doesn't have optional parameters that need to be sent in. a `GET` request will assume `getObject` if you don't specify a method.

```
https://api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234.json
```


### POST
A `POST` request is needed for optional parameters. `POST` assums the `createObject` method if you don't specify one.

This method takes in a single Boolean parameter.
```
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": ["1"]} 
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/12345/toggleManagementInterface.json'`
```

This method takes in a single SoftLayer_Dns_Domain object.
```
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters" : [
    {"name" : "example.org", "resourceRecords" : [{"type" : "a","host" : "@","data" : "127.0.0.1" }]}
]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain.json'
```

>When using POST to send in parameters, the parameter order of the array needs to match the order the parameters appear in the documentation. You don't need to send in the parameter name. 



### PUT
Use an HTTP PUT request to edit an object instead of a service's `editObject() `method. PUT a single JSON or XML structure containing a single element called "parameters" containing your object's skeleton structure and any orther parameters required by your API service's `editObject()` method. For instance, pass an HTTP PUT request with the following data to the following URL in order to edit domain resource record 5678 within domain record 1234 on SoftLayer's DNS servers, changing its `data` to "10.0.0.1".

```
curl -u $SL_USER:$SL_APIKEY -X PUT -d '{"parameters": [{"data": "10.0.0.1",}]}'
https://api.softlayer.com/rest/v3/SoftLayer_Dns_Domain/1234/ResourceRecords/5678.json
```

## Passing Method Parameters

The order (top to bottom) you send in parameters needs to match the order they are listed in the documentation. For example, [SoftLayer_Account::createUser()](/reference/services/SoftLayer_Account/createUser/) takes in 4 parameters, first would be the `templateObject`, then `password`, then `vpnPassword`, then `silentlyCreateFlag`. The data passed in the parameters are treated like an array, so you don't need to include the paramter name anywhere.

There are 2 main ways to pass in parameters. The most consistent, and what I recommend, is by using a `POST` request and sending the parameters as part of the data.

For example [SoftLayer_Monitoring_Agent::setActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscribe) requires the userRecordId parameter:

```
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [5678]}'
'https://api.softlayer.com/rest/v3.1/SoftLayer_Monitoring_Agent/1234/setActiveAlarmSubscriber/'
```

Alternatively, you can put the paramters in the URL for simple types like string, int, and bool. 

```
curl -u $SL_USER:$SL_APIKEY https://api.softlayer.com/rest/v3/SoftLayer_Monitoring_Agent/1234/setActiveAlarmSubscriber/5678.json
```


Some methods will request a single parameter which is an array such as [SoftLayer_Dns_Domain_ResourceRecord::createObjects](/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObjects)
```
{
  "parameters":
    [
      [
        {"host":"hosta","data":"127.0.0.1","ttl":"900","type":"a","domainId":"1234"}
        ,
        {"host":"hostb","data":"127.0.0.1","ttl":"900","type":"a","domainId":"1234"}
      ]
    ]
}
```


## Using Object Masks
Create an [object mask](/article/object mask) in your API call URL by adding an `objectMask` variable to your query string. Object masks are a nested array of relational or local properties. 

The following URL creates an object mask that retrieves an account's hardware records along with the datacenters that hardware is located in. Note that the object mask only contains the relational property we want to retrieve related to hardware, not our account.

```
https://api.softlayer.com/rest/v3/SoftLayer_Account/getHardware.json?objectMask=mask[datacenter]
```


This URL gets an account's hardware records along with that hardware's associated datacenter, operating system, and network component records. Note that these relational items are separate by semicolons.

```
https://api.softlayer.com/rest/v3/SoftLayer_Account/getHardware.json?objectMask=mask[datacenter,operatingSystem,networkComponents]
```


This URL gets an account's hardware records along with that hardware's associated datacenter, operating system, operating system password, and network component records. 

```
https://api.softlayer.com/rest/v3/SoftLayer_Account/Hardware.json?objectMask=mask[datacenter,operatingSystem[passwords],networkComponents]
```

>There are some other ways of specifying object mask, just as `objectMask=datacenter;operatingSystem.passwords;networkComponents`, but for clarity I use the `mask[datacenter,operatingSystem[passwords],networkComponents]` format.

Selecting a `local` property in your objectMask will remove all other local properties on that level of your objectMask. 

## Using Result Limits
Any method that returns an array of values can make use of a resultLimit to page through the results. This is useful if not including the resultLimit makes an API call timeout. 

For example, [SoftLayer_Account::getOpenTickets](/reference/services/SoftLayer_Account/getOpenTickets) returns an array of SoftLayer_Ticket[] (if the return type ends with [] the method is returning an array).

```
https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getOpenTickets.json?resultLimit=0,2
```
**Note:** In the example the offset is 0 and the limit is 2, and in this case we can remove the offset to get the same response (resultLimit=2).

As part of the HTTP return headers, there is a header called `SoftLayer-Total-Items` that will show you how many total results you can expect. 

```shell
curl -v -u $SL_USER:$SL_APIKEY https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getOpenTickets.json?resultLimit=0,2
> GET /rest/v3/SoftLayer_Account/getOpenTickets.json?resultLimit=0,2 HTTP/1.1
> Host: api.softlayer.com
> Authorization: Basic UA==
> User-Agent: curl/7.61.1
> Accept: */*
> Accept-Encoding: gzip, deflate, compress

< HTTP/1.1 200 OK
< Date: Fri, 30 Nov 2018 22:51:16 GMT
< Server: Apache
< X-Frame-Options: SAMEORIGIN
< SoftLayer-Total-Items: 4       # I can expect 4 total openTickets
< Content-Length: 1616
< Vary: Accept-Encoding
< Connection: close
< Content-Type: application/json
< Strict-Transport-Security: max-age=31536000

```

## Error Handling

The SoftLayer REST API returns XML or JSON output with a single <tt>error</tt> node containing any error messages returned by your API call. For instance, the URL to the nonexistent service:

```
https://api.softlayer.com/rest/v3/Nonexistent.xml
```

returns the error:

```xml
<root>
    <error>Service does not exist</error>
    <code>SoftLayer_Exception_Public</code>
</root>
```

<p>While it's JSON equivalent:</p>
```
https://@api.softlayer.com/rest/v3/Nonexistent.json
```

returns the error:

```json
{"error": "Service does not exist"}
```

### Authentication Errors
The SoftLayer REST API returns an HTTP 401 Unauthorized error if an invalid username / API key combination is used when requesting a REST URL.
