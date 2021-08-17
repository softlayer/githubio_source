---
title: "The SoftLayer Golang Library"
description: "Covers how to use the Golang library to make API calls, along with some basics of the IBMCLOUD cli tool, which is written in golang."
date: "2021-08-16"
tags:
    - "tools"
    - "slcli"
    - "article"
    - "go"
---


## The Basics
- [softlayer-go](https://github.com/softlayer/softlayer-go) project homepage. Contains the source code for the library, and a place to submit feature requests and bug reports
- [Golang Example Library](/go/) A collection of examples on how to use softlayer-go to work with the SL API.
- [IBMCLOUD SL](https://github.com/softlayer/softlayer-cli) contains the source code for the `ibmcloud sl` command, any issues with that plugin should be reported to the github page.

--------------

## Authentication
The first thing we need to do before making API calls, is setup our authentication.

Every program that uses the softlayer-go library will first create a Session object to interact with and make API calls through. This Session object will be defined as follows for these examples

```go
package main

import (
    "github.com/softlayer/softlayer-go/datatypes"
    "github.com/softlayer/softlayer-go/filter"
    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
    "github.com/softlayer/softlayer-go/sl"
)
var SLSession = session.New()
```

>NOTE: not all of those imports will be used in all examples, but it is a good starting point and highlights what is commonly used.

When a new [Session](https://github.com/softlayer/softlayer-go#sessions) is established, it gets the authentication information from the following sources.

#### [The ~/.softlayer config](#softlayer-config) {#softlayer-config .anchor-link}

Like with the [softlayer-python](https://github.com/softlayer/softlayer-python) project, softlayer-go reads from the `~/.softlayer` configuration file to find any authentication information.

The basic format is like this:

```
[softlayer]
username = <your username>
api_key = <your api key>
endpoint_url = <optional>
timeout = <optional>
```

#### [Environment Variables](#softlayer-environment) {#softlayer-environment .anchor-link}

softlayer-go reads from the following Environmental Variables, taking precedent over the configuration file.

```
SL_USERNAME or SOFTLAYER_USERNAME
SL_API_KEY or SOFTLAYER_API_KEY
SL_ENDPOINT_URL or SOFTLAYER_ENDPOINT_URL
SL_TIMEOUT or SOFTLAYER_TIMEOUT
```

--------------

## [Making API Calls](#making-api-calls) {#making-api-calls .anchor-link}

Now that we have an authenticated Session created, we are almost ready to make API calls.

#### [SoftLayer Service Classes](#sl-services) {#sl-services .anchor-link}

The softlayer-go library groups each SL API service by that service's group. For example the [softlayer-go/services/hardware](https://github.com/softlayer/softlayer-go/blob/master/services/hardware.go) file contains the [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware/), [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server/) and [SoftLayer_Hardware_Component_Model](/reference/services/SoftLayer_Hardware_Component_Model/) classes, among others. If you are looking at the SLDN documentation, the last tag on the service's SLDN page will tell you which group that service belongs to, and thus which class definition file it exists in.

These service and datatype files are kept updated on a monthly basis if you are using the latest version of the softlayer-go library. While generally these class definitions are only added to, rarely they do change and when that happens you need to either get the newest copy of this library, or update the library services and datatypes manually by running `make generate` in the softlayer-go project main directory.

Once you know what service and method you want to call, you need to create a new instance of that service and assign it to a variable like this.

```go
virtualService := services.GetVirtualGuestService(SLSession)
```

#### [Call properties](#call-properties) {#call-properties .anchor-link}

There are a few other bits of information we might need to send into the API when making our call, and we provide these with a method chain when invoking our API call.

```
apiResult = virtualService.Mask("mask[id,hostname]").Id(123456).GetObject()
```

That will call [SoftLayer_Virtual_Guest.getObject()](/reference/services/SoftLayer_Virtual_Guest/getObject/) with the Id of 123456 and a mask of `mask[id,hostname]`. You can also specify [ObjectFilters, Result Limit and Offset](https://github.com/softlayer/softlayer-go#object-masks-filters-result-limits)

Properties of a call include things like
- [Object Masks](article/object-masks/)
- [Object Filters](/article/object-filters/)
- [Result Limit and Offset](/article/using-result-limits-softlayer-api/)
- [Init Parameters](/article/using-initialization-parameters-softlayer-api/)

In the golang library, these are defined in the [sl.Options](https://github.com/softlayer/softlayer-go/blob/master/sl/options.go) type.

#### [Call Parameters](#call-param) {#call-param .anchor-link}

When passing parameters into an API call (which are listed explicitly in the documentation, and are different from properties) you do so by adding them to the method's call.

```go
objectTemplate := datatypes.Hardware_Server{
    Notes: sl.String("Just some notes"),
}
hardwareService := services.GetHardwareServerService(SLSession)
result, err := hardwareService.Id(123456).EditObject(&objectTemplate)
```

From the documentation for [SoftLayer_Hardware_Server::editObject](/reference/services/SoftLayer_Hardware_Server/editObject/) we can see that this method takes in 1 parameter, which is of type Hardware_server. If a method takes in more than 1 parameter, these will be specified in order, but NOT by name as listed in the documentation. The name in the documentation is just to give you an idea what that parameter is for, there is no way to send in parameters by name.


#### [Error Checking](#error-checking) {#error-checking .anchor-link}

Every API call will return an error object as well as a result object. The [softlayer-go readme](https://github.com/softlayer/softlayer-go#handling-errors) has some good examples on this, but the basics would look like this.

> Note that [sl.Error](https://github.com/softlayer/softlayer-go/blob/master/sl/errors.go) implements the standard error interface, so it can be handled like any other error, if the above granularity is not needed:

```go
_, err := service.GetObject()
if err != nil {
    fmt.Println("Error during processing: ", err)
}
```

--------------

## [Debugging](#debugging) {#debugging .anchor-link}

Some times it can be useful to see what exact API call the library is making, and to do that simply enable debugging in the Session and the API calls will be logged and printed to STDOUT by default.

```go
SLSession.debug = True
// If you want to redirect the logs to somewhere else.
session.Logger = log.New(os.Stderr, "[CUSTOMIZED] ", log.LstdFlags)
```

With debugging enabled, any request sent to the SL API and any response returned will be logged. If you ever need to report any API issues to IBM this output is critical in getting the issue properly resolved.

--------------

## [Ibmcloud SL](#ibmcloud-sl) {#ibmcloud-sl .anchor-link}

The [IBMCLOUD CLI](https://www.ibm.com/cloud/cli) is a tool written in golang, and has a `sl` subcommand that uses the softlayer-go library to make all of its API calls. If you ever have any issues with this subcommand, make sure to open an issue on our [softlayer-cli github](https://github.com/softlayer/softlayer-cli) page to let us know about it.


