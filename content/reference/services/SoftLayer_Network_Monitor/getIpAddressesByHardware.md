---
title: "getIpAddressesByHardware"
description: "This will return an arrayObject of objects containing the ipaddresses.  Using an string parameter you can send a partial... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor"
aliases:
    - "/reference/services/softlayer_network_monitor/getIpAddressesByHardware"
---
# [SoftLayer_Network_Monitor](/reference/services/SoftLayer_Network_Monitor)::getIpAddressesByHardware

Returns an ArrayObject of subnet ip address objects for a hardware


## Overview 
This will return an arrayObject of objects containing the ipaddresses.  Using an string parameter you can send a partial ipaddress to search within a given ipaddress.  You can also set the max limit as well using the setting the resultLimit. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardware| <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>| The hardware object.|
|partialIpAddress| string| A partial ipaddress is sent.|


### Required Headers
* authenticate


### Optional Headers
* resultLimit

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>




