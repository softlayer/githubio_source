---
title: "createObject"
description: "Create a new firewall update request. The SoftLayer_Network_Firewall_Update_Request object passed to this function must... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
aliases:
    - "/reference/services/softlayer_network_firewall_update_request_rule/createObject"
---
# [SoftLayer_Network_Firewall_Update_Request_Rule](/reference/services/SoftLayer_Network_Firewall_Update_Request_Rule)::createObject


Create a new firewall update request rule.


## Overview 
Create a new firewall update request. The SoftLayer_Network_Firewall_Update_Request object passed to this function must have at least one rule. 

''createObject'' returns a Boolean ''true'' on successful object creation or ''false'' if your firewall update request was unable to be created.. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule'>SoftLayer_Network_Firewall_Update_Request_Rule </a>| The SoftLayer_Network_Firewall_Update_Request_Rule object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Firewall_Update_Request_RuleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule'>SoftLayer_Network_Firewall_Update_Request_Rule </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "At least one valid rule is required to create a a firewall update request." if the firewall update request in the templateObject parameter doesn't have at least one rule record. 



