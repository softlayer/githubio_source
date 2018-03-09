---
title: "verifyReloadOperatingSystem"
description: "Verify that a virtual server can go through the operating system reload process. It may be useful to call this method be... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::verifyReloadOperatingSystem

Verify that a virtual server can go through the operating system reload process.


## Overview 
Verify that a virtual server can go through the operating system reload process. It may be useful to call this method before attempting to actually reload the operating system just to verify that the reload will go smoothly. If the server configuration is not setup correctly or there is some other issue, an exception will be thrown indicating the error. If there were no issues, this will just return true. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|config| <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration'>SoftLayer_Container_Hardware_Server_Configuration </a>| The new cloud configuration for the reload.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
boolean

