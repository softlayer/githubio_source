---
title: "getObject"
description: "getObject returns a SoftLayer_Network_Firewall_Update_Request_Rule object. You can only get historical objects for serve... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
---
# [SoftLayer_Network_Firewall_Update_Request_Rule](/reference/services/SoftLayer_Network_Firewall_Update_Request_Rule)::getObject

Retrieve a SoftLayer_Network_Firewall_Update_Request_Rule record.


## Overview 
getObject returns a SoftLayer_Network_Firewall_Update_Request_Rule object. You can only get historical objects for servers attached to your account that have a network firewall enabled. createObject inserts a new SoftLayer_Network_Firewall_Update_Request_Rule object. Use the SoftLayer_Network_Firewall_Update_Request to create groups of rules for an update request. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Firewall_Update_Request_RuleInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Firewall_Update_Request_RuleObjectMask
* SoftLayer_Network_Firewall_Update_Request_RuleObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule'>SoftLayer_Network_Firewall_Update_Request_Rule </a>

