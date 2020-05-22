---
title: "getPrivateVlanByIpAddress"
description: "*** DEPRECATED ***
Retrieve a backend network VLAN by searching for an IP address"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getPrivateVlanByIpAddress"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getPrivateVlanByIpAddress

Retrieve a backend network VLAN by searching for an IP address.


## Overview 

*** DEPRECATED ***
Retrieve a backend network VLAN by searching for an IP address 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The server's IP address you are searching for.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Hardware_SecurityModule750ObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "You must provide a valid IP address." if an invalid IPV4 IP address was provided. 

* SoftLayer_Exception 

> Throw the exception "Unable to find a subnet." if there is no subnet for the IP address provided. 

* SoftLayer_Exception 

> Throw the exception "Unable to find a valid network component for this IP address." if a network component with the primary IP address the same as the one provided could not be found. 



