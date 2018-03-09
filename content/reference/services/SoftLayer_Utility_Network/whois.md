---
title: "whois"
description: "Perform a WHOIS lookup from SoftLayer's application servers on the given IP address or hostname and return the raw resul... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Utility"
classes:
    - "SoftLayer_Utility_Network"
---
# [SoftLayer_Utility_Network](/reference/services/SoftLayer_Utility_Network)::whois

Perform a WHOIS lookup on a given address.


## Overview 
Perform a WHOIS lookup from SoftLayer's application servers on the given IP address or hostname and return the raw results of that command. The returned result is similar to the result received from running the command `whois` from a UNIX command shell. A WHOIS lookup queries a host's registrar to retrieve domain registrant information including registration date, expiry date, and the administrative, technical, billing, and abuse contacts responsible for a domain. WHOIS lookups are useful for determining a physical contact responsible for a particular domain. WHOIS lookups are also useful for determining domain availability. Running a WHOIS lookup on an IP address queries ARIN for that IP block's ownership, and is helpful for determining a physical entity responsible for a certain IP address. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|address| string| An IP address or hostname to whois.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
string

### External Links


* [WHOIS at Wikipedia](http://en.wikipedia.org/wiki/WHOIS)


* [RFC 3912 - WHOIS Protocol Specification at ietf.org](http://tools.ietf.org/html/rfc3912)



### associatedMethods

*  [SoftLayer_Utility_Network::ping](/reference/services/SoftLayer_Utility_Network/ping )
*  [SoftLayer_Utility_Network::traceroute](/reference/services/SoftLayer_Utility_Network/traceroute )
*  [SoftLayer_Utility_Network::nslookup](/reference/services/SoftLayer_Utility_Network/nslookup )

