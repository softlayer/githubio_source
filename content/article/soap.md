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


<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc7">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#WSDL_URLs_and_Files">WSDL URLs and Files</a></li>
<li class="toc-level-1"><a href="#Sending_API_Call_Headers">Sending API Call Headers</a></li>
<li class="toc-level-1"><a href="#Using_Object_Masks">Using Object Masks</a></li>
<li class="toc-level-1"><a href="#Using_Result_Limits">Using Result Limits</a></li>
<li class="toc-level-1"><a href="#Error_Handling">Error Handling</a></li>
<li class="toc-level-1"><a href="#Caveats">Caveats</a>
<ol>
<li class="toc-level-2"><a href="#WSDL_and_XSD_File_Sizes">WSDL and XSD File Sizes</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#External_Links">External Links</a></li>
</ol>
</div>
</div>
SoftLayer provides a SOAP interface in addition to [[XML-RPC]] and [[REST]]. We recommend using the SOAP API, as it is the most comprehensive API that we currently offer.
## WSDL URLs and Files
The SoftLayer SOAP API has one endpoint per available API service. Each endpoint has a unique URL containing the service name of the API service that it calls.  For example:
<code>
https://api.softlayer.com/soap/v3/<serviceName>?wsdl
</code>
or
<code>
http://api.service.softlayer.com/soap/v3/<serviceName>?wsdl
</code>
In these examples, <code>"<serviceName>"</code> would be replaced with the name of the API services you wish to call. Use the second URL to access the SOAP API over SoftLayer's private network. It's a faster, more secure way to communicate with SoftLayer, but the system making API calls must be on SoftLayer's private network.  All SoftLayer servers come with access to our private network, including CCIs.  Additional private IP addresses are available for purchase should they be needed.

Each WSDL defines that specific service's available methods and includes an XSD file that defines every complex type available to the SoftLayer API. Once a WSDL is imported by your consuming service,  every data type and API service method should be available in your project.
## Sending API Call Headers
Important API headers, such as authentication, initialization parameters, and object masks are sent to the SoftLayer API as SOAP headers. Each call header has an associated complex type. This sample header contains authentication information and an initialization parameter for the [[SoftLayer_Hardware_Server]] API service.

```
<xml>
<SOAP-ENV:Header>
    <ns1:authenticate>
        <username>set me</username>
        <apiKey>set me too</apiKey>
    </ns1:authenticate>
    <ns1:SoftLayer_Hardware_ServerInitParameters>
        <id>1234</id>
    </ns1:SoftLayer_Hardware_ServerInitParameters>
</SOAP-ENV:Header>
</xml>
```

## Using Object Masks
Add an [[object mask]] to your API call by adding an object mask complex type which corresponds to the API service you are calling. Object masks are named according to your API servicewith a "<code><serviceName></code>ObjectMask" format, where <code><serviceName></code> corresponds to the name of the API service you're calling. For instance, an object mask for the SoftLayer_Account API service has the name <code>SoftLayer_AccountObjectMask</code> and the SoftLayer_Hardware_Server service's corresponding object mask class name is <code>SoftLayer_Hardware_ServerObjectMask</code>.
Declare a <code><mask></code> inside your object with the name "mask" of the type defined by your API service containing the relational and count properties you wish to retrieve along with your API call result. Each item in your object mask is an empty XML value.

This example retrieves the following information:

* The account's physical hardware records 
* That hardware's operating system record 
* Operating system passwords 
* Network components 
* Datacenter in which the hardware is located 
* Number of processors in each hardware:

```xml
<xml>
<SoftLayer_Hardware_ServerObjectMask xsi:type="v3:SoftLayer_Hardware_ServerObjectMask">
    <mask xsi:type="slt:SoftLayer_Hardware_Server" xmlns:slt="https://api.softlayer.com/soap/v3/SLTypes/">
        <operatingSystem>
            <passwords />
        </operatingSystem>
        <datacenter />
        <processorCount />
    </mask>
</SoftLayer_Hardware_ServerObjectMask>
</xml>
```

## Using Result Limits
Place a result limit in your API call by adding a <code>resultLimit</code> complex type to your call headers. The resultLimit object has two properties:

* "limit", an integer representing the number of results to limit your call.
* "offset", an integer offset to begin your result set.
This resultLimit header represents a result with a limit of 2, starting at offset 0.

```xml
<xml>
<resultLimit xsi:type="slt:resultLimit" xmlns:slt="http://api.service.softlayer.com/soap/v3/SLTypes/">
    <limit xsi:type="xsd:int">2</limit>
    <offset xsi:type="xsd:int">0</offset>
</resultLimit>
</xml>
```

## Error Handling
The SOAP API returns SOAP faults if your call encounters an error. The fault's <code>faultcode</code> corresponds to the type of exception thrown by your error, while the fault's <code>faultstring</code> contains your error message.
## Caveats
### WSDL and XSD File Sizes
Depending on the API service you request, your WSDL consuming service may download over a megabyte of information when it downloads a WSDL file. The WSDL's included XSD defines every data type available at SoftLayer and is rather large. Your first API call may take some time while the WSDL is downloaded and processed. We highly recommend local WSDL and XSD caching so repeated calls don't take as long.

## External Links
* [http://www.w3.org/TR/soap/ SOAP Specifications]
* [http://en.wikipedia.org/wiki/SOAP SOAP] at [http://www.wikipedia.org/ Wikipedia]