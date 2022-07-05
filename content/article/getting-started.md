---
title: "Getting Started"
description: "Basics for the SoftLayer API"
date: "2020-10-26"
tags:
    - "article"
    - "sldn"
---

# Introduction to the SoftLayer API

<iframe width="100%" height="630" src="https://www.youtube.com/embed/SFSmaX9CEAQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[slides](/apiVideo01-Basics.md.html)

Welcome to SLDN, the home of the documentation for the SoftLayer, or IBM Classic Infrastructure, API. Here you can find a collection of [Articles](/article/) that cover some of the core concepts in details, [Reference Documentation](/reference/softlayerapi/) which is the automatically generated API specifications and documentation, and also a collection of examples in a variety of programming languages like [Golang](/go/), [Python](/python/), and [Java](/java/)

## Before You Start
### Choosing a Protocol
SoftLayer's API can be accessed by [SOAP](/article/soap/), [XML-RPC](/article/xml-rpc), or [REST](/article/rest/). Choose the best protocol for your preferred language and situation. The SOAP endpoint will be the most precise, but anything you can do in the SOAP endpoint can be done in REST or XML-RPC.

If you just want to make a few simple API calls, REST is likely the easiest to pick up and start working with.

|Protocol |Advantages |Disadvantages | Recommended For | Recommended Languages|
| ---       |   ---        |       ---       |  ----     |----     |
|[SOAP](/article/soap/)| It's the fastest of the three protocols and allows you to make direct calls against SoftLayer's API services and data types. | Initial WSDL consumption may take some time. | Calling SoftLayer API services as code local to your project. | [C-Sharp](/csharp/), [Perl](/perl), [PHP](/php)|
|[XML-RPC](/article/xml-rpc) | Wide support amongst programming languages. | Lack of complex type specifications may require extra work when working with specific data types. |  Making API calls in languages without proper SOAP support. | [PHP](/php), [Python](/python) |
| [REST](/article/rest/) | Most programming languages support standard HTTP protocol operations if they don't have explicit support for SOAP or XML-RPC. |  REST URLs can become complex, especially when working with complex data structures. | Quickly calling get*() methods and retrieving data with a minimum amount of hierarchy. | [Ruby](/ruby), [Go](/go), [Java](/java), Any language that supports standard HTTP protocol operations, JSON parsing, and XML parsing

### Getting Your API Key
API calls are authenticated by the username you use to authenticate to the SoftLayer portal and a special [API Key](/article/authenticating-softlayer-api/). You'll have the most access by using your account's master user to make API calls, but your code may be more secure if you use a sub-account with a more limited permission set.

### Using The Private Network
SoftLayer has API endpoints listening on the private network. Private network calls can only be made from systems on the private network, either from servers or computing instances purchased from SoftLayer or from systems VPN'd into the private network. On the other hand private network calls aren't made over the public Internet. They're more secure and take less time to execute.

To use the private network in your API call replace `https://api.softlayer.com` with `https://api.service.softlayer.com`. 

-----------------------------------

## Core Concepts
This article will focus mainly on the specifics of the REST interface, as it is the simplest to learn. Everything covered here will apply to the SOAP and XMLRPC interfaces as well, the only difference will be in how you format the request.
    - Learn more about [SOAP Api Calls](/article/soap/)
    - Learn more about [XML-RPC API Calls](/article/xml-rpc/)

### URL Format

<pre>
'https://api.softlayer.com/rest/v3.1/<font color="red">[SERVICE]</font>/<font color="Coral">[INIT PARAMETER]</font>/<font color="blue">[METHOD]</font><font color="green">.json</font>?<font color="teal">[objectMask]</font>&<font color="BlueViolet">[objectFilter]</font>&<font color="DarkOrange">[RESULT LIMIT]</font>'
</pre>

#### <font color="red">[SERVICE](#service-format)</font> {#service-format .anchor-link}
Indicates which specific service out of the [Services List](https://sldn.softlayer.com/reference/) you want to interact with. [SoftLayer_Account](/reference/services/SoftLayer_Account/) or [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest/) are examples of services.

A service is a way to group actions (aka methods) that all perform actions related to each other in some way. The SoftLayer_Account service will deal with account actions, SoftLayer_Hardware_Server service will deal with bare metal servers and so forth.

#### <font color="Coral">[INIT PARAMETER](#init-parameter)</font> {#init-parameter .anchor-link}
If in the documentation for a API call, you see something like `SoftLayer_DatatypeInitParameters` in the `Required Headers` portion, that indicates you need to send in the appropriate `id` for the request. [SoftLayer_Virtual_Guest::getObject()](/reference/services/SoftLayer_Virtual_Guest/getObject/) for examples requires a `SoftLayer_Virtual_GuestInitParameters`, which means you need to send in the `id` of the virtual guest you want to access.

To get a list of virtual guest ids for example, you could use [SoftLayer_Account::getVirtualGuests()](/reference/services/SoftLayer_Account/getVirtualGuests/). The SoftLayer_Account service is a bit special in that it generally doesn't require any `SoftLayer_AccountInitParameters`. This is because it assumes you are using the SoftLayer_Account id associated with the account making API calls.

#### <font color="blue">[METHOD](#the-method)</font> {#the-method .anchor-link}
Each service will have a SLDN page dedicated to it, which will list out all its available methods that can be called. Each method in turn will have a page dedicated to explaining what it does, and what required and optional headers are available along with the parameters you need to supply. 

#### <font color="green">[.json](#return-format)</font> {#return-format .anchor-link}
This tells the API how to format the data when you get it back. Also available are .xml and .txt

#### <font color="teal">[objectMask](#objectMask)</font> {#objectMask .anchor-link}
The [objectMask](/article/object-masks/) allows you to modify the data returned by adding or removing properties that the method's return datatype will be. Generally this will just be a string like `objectMask=mask[id,property1,property2[nested1,nested2]]`. Methods that allow this will have `SoftLayer_ObjectMask` or `SoftLayer_Data_TypeObjectMask` as a optional header. Any property you add here that isn't valid will result in an API error.


#### <font color="BlueViolet">[objectFilter](#objectFilter)</font> {#objectFilter .anchor-link}
The [objectFilter](/article/object-filters/) allow you to fine tune which results in a list get sent back, and these can get quite complicated. They are formatted like JSON objects and need to be parseable as such.

> <font color="red">**WARNING**</font></p>
> Filters that don't properly tap into properties can be silently ignored, be sure to check your filter is working as expected.

#### <font color="DarkOrange">[RESULT LIMIT](#resultLimit)</font>  {#resultLimit .anchor-link}
Any method that has a `resultLimit` optional header can use this to paginate through the result set, allowing you to get through a dataset that might be otherwise be too large for a single api call, generating [timeouts and other API errors](/article/how-solve-error-fetching-http-headers/). The format is `resultLimit=0,100`. 0 Being the Start Index, and 100 being the count of objects you want returned.

> <font color="red">**WARNING**</font></p>
> Specifying a count of 1 like `resultLimit=0,1` can in some cases result in only the first result being returned, no matter the start index. Always use at least a count of 2 or higher to avoid this.


#### [Datatypes](#the-datatypes) {#the-datatypes .anchor-link}

The data returned to you will usually be a specific datatype, or a base type (like int, string etc), and will have a link to the appropriate SLDN page on the method's documentation. Any datatype that ends with `[]` means you will get an array of those datatypes back.

You can think of a datatype as baiscally a table in a SQL database. The `local` properties are columns in that table, and the `relational` properties are columns in other tables that you can access with a join (using an objectMask for example).

The base datatype is the `SoftLayer_Entity`, which you may see reference to on any method that can take in a variety of different datatypes as a parameter.

#### [Parameters](#the-paramters) {#the-paramters .anchor-link}

Some methods will require parameters to be sent in, for example [SoftLayer_Virtual_Guest::getBandwidthForDateRange()](/reference/services/SoftLayer_Virtual_Guest/getBandwidthForDateRange/) takes 2 parameters, a `startDate` and an `endDate`. 

The most consistent way to send in parameters to the API is as a `POST` request, the structure of which would look like this:

```bash
curl  -u $SL_USER:$SL_APIKEY -X POST  -d '{"parameters": ["2020-10-01", "2020-10-26"]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/107879710/getBandwidthForDateRange.json'
```
>**NOTE**</p>
>The ORDER of these parameters is important, but the name is not.

The format here is a JSON parseable string, with the first element of the base object being `parameters`, which is an array that matches the method's documentation. Any parameters that are marked as a datatype themself will be a JSON object. When specifying a datatype as a parameter, you usually only have a pass in a few key fields, like `id`, not an entirely fleshed out object.

For example, [SoftLayer_Virtual_Guest::editObject()] takes in 1 virtual guest datatype, a request would look like this:

```
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [{"hostname": "test1234"}]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/106291032/editObject.json'
```

-------------------------------------------

## Open Source SDKs and CLI tools
SoftLayer maintains a variety of SDKs to help in making API calls easier. All of which can be found in the official [softlayer github.com repository](https://github.com/softlayer)

- [Python Library and SL CLI tool](https://github.com/softlayer/softlayer-python). 
    -  A python based CLI tool. Has a [slcli call-api](https://softlayer-python.readthedocs.io/en/latest/cli/commands/#call-api) function that makes command line API calls easy.
- [ibmcloud CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started). 
    - A CLI tool that uses the softlayer-go library, includes a `ibmcloud sl call-api` function that makes writing API calls on the command line easy.
- [Golang](https://github.com/softlayer/softlayer-go)
- [Java](https://github.com/softlayer/softlayer-java)
- [PHP](https://github.com/softlayer/softlayer-api-php-client)
- [Ruby](https://github.com/softlayer/softlayer-ruby)
- [Perl](https://github.com/softlayer/softlayer-api-perl-client)

## Where To Go From Here

The [SoftLayer_Account](/reference/services/SoftLayer_Account) service is an umbrella service. Everything relates back to your account record, your inventory, accounting records, domains, support tickets, and everything else. Where you go from here depends solely on what you're trying to accomplish. Make a few more queries to the SoftLayer_Account service to see what data types are returned. Try out a few [object mask](/article/object-masks/) to see how our data types relate to each other. If you need to work with another service then head to its manual page to see what you can do with it. Here are a few of the more common services used:

*   [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server): Access information related to hardware purchased from SoftLayer.
*   [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest): Access and automate CloudLayer Computing Instances.
*   [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain): Create and manage domains in SoftLayer's DNS infrastructure.
*   [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket): Create and update support tickets.
*   [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer): Manage your account's portal, forum, VPN, and API users.
*   [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item): Find out more information about what will show up on your next invoice.
*   [SoftLayer_Billing_Invoice](/reference/services/SoftLayer_Billing_Invoice): Access your previous invoices and audit what you've been paying for since you opened your account.
*   [SoftLayer_Product_Order](/reference/services/SoftLayer_Product_Order): Place orders for new or upgrade your existing SoftLayer services.