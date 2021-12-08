---
title: "updateNetScalerLicense"
description: "Update the NetScaler VPX License. 

This service will create a transaction to update a NetScaler VPX License.  After the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
aliases:
    - "/reference/services/softlayer_network_application_delivery_controller/updateNetScalerLicense"
---
# [SoftLayer_Network_Application_Delivery_Controller](/reference/services/SoftLayer_Network_Application_Delivery_Controller)::updateNetScalerLicense


Update the NetScaler VPX License.


## Overview 
Update the NetScaler VPX License. 

This service will create a transaction to update a NetScaler VPX License.  After the license is updated the load balancer will reboot in order to apply the newly issued license 

The load balancer will be unavailable during the reboot. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters


### Optional Headers
* SoftLayer_Network_Application_Delivery_ControllerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>



### Error Handling

* SoftLayer_Exception_Hardware_Server_ActiveTransactionExists 

> Throws the exception 'There is currently an outstanding transaction for this load balancer.' when a load balancer currently has a running transaction. 



