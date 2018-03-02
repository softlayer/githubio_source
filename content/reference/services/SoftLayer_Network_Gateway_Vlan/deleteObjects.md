---
title: "deleteObjects"
description: "Detach several VLANs. This will not detach them right away, but rather start an asynchronous process to detach."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Vlan"
---
# SoftLayer_Network_Gateway_Vlan::deleteObjects
## Overview 
Detach several VLANs. This will not detach them right away, but rather start an asynchronous process to detach. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Gateway_Vlan'>SoftLayer_Network_Gateway_Vlan[] </a>| An array of skeleton SoftLayer_Network_Gateway_Vlan objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

