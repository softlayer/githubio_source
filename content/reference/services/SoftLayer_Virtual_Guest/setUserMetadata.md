---
title: "setUserMetadata"
description: "Sets the data that will be written to the configuration drive."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/setUserMetadata"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::setUserMetadata


Configures the guest's metadata disk.


## Overview 
Sets the data that will be written to the configuration drive. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|metadata| array of strings| base64 encoded strings that will be written to the configuration drive|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Return Values
* boolean




