---
title: "SOAP"
description: "How to interact with the SoftLayer SOAP endpoint"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "soap"
author: "sldn"
---


SoftLayer provides a SOAP interface in addition to [XML-RPC](/article/xml-rpc) and [REST](/article/rest). We recommend using the SOAP API, as it is the most comprehensive API that we currently offer.

## WSDL URLs and Files
The SoftLayer SOAP API has one endpoint per available API service. Each endpoint has a unique URL containing the service name of the API service that it calls.  For example: `https://api.softlayer.com/soap/v3/<serviceName>?wsdl`
or `http://api.service.softlayer.com/soap/v3/<serviceName>?wsdl`

In these examples, `"<serviceName>"` would be replaced with the name of the API services you wish to call. Use the second URL to access the SOAP API over SoftLayer's private network. It's a faster, more secure way to communicate with SoftLayer, but the system making API calls must be on SoftLayer's private network.  All SoftLayer servers come with access to our private network, including CCIs.  Additional private IP addresses are available for purchase should they be needed.

Each WSDL defines that specific service's available methods and includes an XSD file that defines every complex type available to the SoftLayer API. Once a WSDL is imported by your consuming service,  every data type and API service method should be available in your project.


## Your First API Call

The [SoftLayer_Account/getObject|getObject()](/reference/services/SoftLayer_Account/getObject/) method in the [SoftLayer_Account](/reference/services/SoftLayer_Account/) service is a simple call that only requires an authentication header. It returns basic, top-level information about your SoftLayer account and is a great way to test your first API call. Here are a few ways to get it going:

### Raw SOAP
```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="https://api.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <SOAP-ENV:Header>
        <ns1:authenticate>
            <username>set me</username>
            <apiKey>set me too</apiKey>
        </ns1:authenticate>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:getObject/>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

## Sending API Call Headers
Important API headers, such as authentication, initialization parameters, and object masks are sent to the SoftLayer API as SOAP headers. Each call header has an associated complex type. This sample header contains authentication information and an initialization parameter for the [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server) API service.

```xml
<SOAP-ENV:Header>
    <ns1:authenticate>
        <username>set me</username>
        <apiKey>set me too</apiKey>
    </ns1:authenticate>
    <ns1:SoftLayer_Hardware_ServerInitParameters>
        <id>1234</id>
    </ns1:SoftLayer_Hardware_ServerInitParameters>
</SOAP-ENV:Header>
```

## Using Object Masks
Add an [object mask](/article/object-mask) to your API call by adding an object mask complex type which corresponds to the API service you are calling. Object masks are named according to your API service with a `"<serviceName>ObjectMask"` format, where `<serviceName>` corresponds to the name of the API service you're calling. For instance, an object mask for the SoftLayer_Account API service has the name `SoftLayer_AccountObjectMask` and the SoftLayer_Hardware_Server service's corresponding object mask class name is `SoftLayer_Hardware_ServerObjectMask`.
Declare a `<mask>` inside your object with the name "mask" of the type defined by your API service containing the relational and count properties you wish to retrieve along with your API call result. Each item in your object mask is an empty XML value.

This example retrieves the following information:

* The account's physical hardware records 
* That hardware's operating system record 
* Operating system passwords 
* Network components 
* Datacenter in which the hardware is located 
* Number of processors in each hardware:

```xml
<SoftLayer_Hardware_ServerObjectMask xsi:type="v3:SoftLayer_Hardware_ServerObjectMask">
    <mask xsi:type="slt:SoftLayer_Hardware_Server" xmlns:slt="https://api.softlayer.com/soap/v3/SLTypes/">
        <operatingSystem>
            <passwords />
        </operatingSystem>
        <datacenter />
        <processorCount />
    </mask>
</SoftLayer_Hardware_ServerObjectMask>
```

## Using Result Limits
Place a result limit in your API call by adding a <code>resultLimit</code> complex type to your call headers. The resultLimit object has two properties:

* "limit", an integer representing the number of results to limit your call.
* "offset", an integer offset to begin your result set.
This resultLimit header represents a result with a limit of 2, starting at offset 0.

```xml
<resultLimit xsi:type="slt:resultLimit" xmlns:slt="http://api.service.softlayer.com/soap/v3/SLTypes/">
    <limit xsi:type="xsd:int">2</limit>
    <offset xsi:type="xsd:int">0</offset>
</resultLimit>
```

## Error Handling
The SOAP API returns SOAP faults if your call encounters an error. The fault's `faultcode` corresponds to the type of exception thrown by your error, while the fault's `faultstring` contains your error message.

## Caveats

### WSDL and XSD File Sizes

Depending on the API service you request, your WSDL consuming service may download over a megabyte of information when it downloads a WSDL file. The WSDL's included XSD defines every data type available at SoftLayer and is rather large. Your first API call may take some time while the WSDL is downloaded and processed. We highly recommend local WSDL and XSD caching so repeated calls don't take as long.

## External Links

* [SOAP Specifications](http://www.w3.org/TR/soap/)
* [ Wikipedia](http://en.wikipedia.org/wiki/SOAP)
