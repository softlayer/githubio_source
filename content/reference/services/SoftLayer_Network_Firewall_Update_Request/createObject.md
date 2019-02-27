---
title: "createObject"
description: "Create a new firewall update request. The SoftLayer_Network_Firewall_Update_Request object passed to this function must... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request"
aliases:
    - "/reference/services/softlayer_network_firewall_update_request/createObject"
---
# [SoftLayer_Network_Firewall_Update_Request](/reference/services/SoftLayer_Network_Firewall_Update_Request)::createObject

Create a new firewall update request.


## Overview 
Create a new firewall update request. The SoftLayer_Network_Firewall_Update_Request object passed to this function must have at least one rule. 

''createObject'' returns a Boolean ''true'' on successful object creation or ''false'' if your firewall update request was unable to be created. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request </a>| The SoftLayer_Network_Firewall_Update_Request object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Firewall_Update_RequestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "At least one valid rule is required to create a firewall update request." if the firewall update request in the templateObject parameter doesn't have at least one rule record. 



