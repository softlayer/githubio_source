---
title: "nsLookup"
description: "A method used to return the nameserver information for a given address"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Utility"
classes:
    - "SoftLayer_Utility_Network"
aliases:
    - "/reference/services/softlayer_utility_network/nsLookup"
---
# [SoftLayer_Utility_Network](/reference/services/SoftLayer_Utility_Network)::nsLookup

Perform a nameserver lookup on given address.


## Overview 
A method used to return the nameserver information for a given address

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|address| string| An IP address or hostname to nslookup.|
|type| string| The type of record to return A, MX, NS, CNAME, TXT.|


### Required Headers
* authenticate


### Return Values
* string

### External Links


* [nslookup at Wikipedia](http://en.wikipedia.org/wiki/Nslookup)



### Associated Methods

*  [SoftLayer_Utility_Network::ping](/reference/services/SoftLayer_Utility_Network/ping )
*  [SoftLayer_Utility_Network::traceroute](/reference/services/SoftLayer_Utility_Network/traceroute )
*  [SoftLayer_Utility_Network::whois](/reference/services/SoftLayer_Utility_Network/whois )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Please provide an address to nslookup." if the address parameter is empty. 

* SoftLayer_Exception_Public 

> Throw the exception "Please provide a valid IP address or hostname." if the address parameter is not a valid IP address or hostname. 



