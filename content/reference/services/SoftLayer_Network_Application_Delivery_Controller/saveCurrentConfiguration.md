---
title: "saveCurrentConfiguration"
description: "Save an application delivery controller's configuration state. The notes property for this method is optional."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller/saveCurrentConfiguration"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::saveCurrentConfiguration


Save an application delivery controller's configuration state.


## Overview 
Save an application delivery controller's configuration state. The notes property for this method is optional. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|notes| string| A note to identify a saved configuration at a later date.|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters


### Optional Headers
* SoftLayer_Network_Application_Delivery_ControllerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_Configuration_History'>SoftLayer_Network_Application_Delivery_Controller_Configuration_History </a>


### Associated Methods

*  [SoftLayer_Network_Application_Delivery_Controller::restoreConfiguration](/reference/services/SoftLayer_Network_Application_Delivery_Controller/restoreConfiguration )
*  [SoftLayer_Network_Application_Delivery_Controller::restoreBaseConfiguration](/reference/services/SoftLayer_Network_Application_Delivery_Controller/restoreBaseConfiguration )




