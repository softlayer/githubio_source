---
title: "getObject"
description: "''getObject'' returns a SoftLayer_Network_Firewall_Update_Request object. You can only get historical objects for server... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request"
---
# [SoftLayer_Network_Firewall_Update_Request](/reference/services/SoftLayer_Network_Firewall_Update_Request)::getObject

Retrieve a SoftLayer_Network_Firewall_Update_Request record.


## Overview 
''getObject'' returns a SoftLayer_Network_Firewall_Update_Request object. You can only get historical objects for servers attached to your account that have a network firewall enabled. ''createObject'' inserts a new SoftLayer_Network_Firewall_Update_Request object. You can only insert requests for servers attached to your account that have a network firewall enabled. ''getFirewallUpdateRequestRuleAttributes'' Get the possible attribute values for a firewall update request rule. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Firewall_Update_RequestInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Firewall_Update_RequestObjectMask
* SoftLayer_Network_Firewall_Update_RequestObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request </a>

