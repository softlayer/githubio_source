---
title: "getIpAddressesByVirtualGuest"
description: "This will return an arrayObject of objects containing the ipaddresses.  Using an string parameter you can send a partial... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor"
---
# SoftLayer_Network_Monitor::getIpAddressesByVirtualGuest
## Overview 
This will return an arrayObject of objects containing the ipaddresses.  Using an string parameter you can send a partial ipaddress to search within a given ipaddress.  You can also set the max limit as well using the setting the resultLimit. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|guest| <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>| The virtual guest object.|
|partialIpAddress| string| A partial ipaddress is sent.|


### Required Headers
* authenticate

### Optional Headers
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>

