---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Application_Delivery_Controller object whose ID number corresponds to the ID n... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::getObject

Retrieve a SoftLayer_Network_Application_Delivery_Controller record.


## Overview 
getObject retrieves the SoftLayer_Network_Application_Delivery_Controller object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Application_Delivery_Controller service. You can only retrieve application delivery controllers that are associated with your SoftLayer customer account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Application_Delivery_ControllerInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Application_Delivery_ControllerObjectMask
* SoftLayer_Network_Application_Delivery_ControllerObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller </a>

