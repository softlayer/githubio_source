---
title: "validateRule"
description: "Validate the supplied firewall request rule against the object it will apply to. For IPv4 rules, pass in an instance of... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
aliases:
    - "/reference/services/softlayer_network_firewall_update_request_rule/validateRule"
---
# [SoftLayer_Network_Firewall_Update_Request_Rule](/reference/services/SoftLayer_Network_Firewall_Update_Request_Rule)::validateRule

Validate a firewall update request rule.


## Overview 
Validate the supplied firewall request rule against the object it will apply to. For IPv4 rules, pass in an instance of SoftLayer_Network_Firewall_Update_Request_Rule. for IPv6 rules, pass in an instance of SoftLayer_Network_Firewall_Update_Request_Rule_Version6. The ID of the applied to object can either be applyToComponentId (an ID of a SoftLayer_Network_Component_Firewall) or applyToAclId (an ID of a SoftLayer_Network_Firewall_Module_Context_Interface_AccessControlList). One, and only one, of applyToComponentId and applyToAclId can be specified. 

If validation is successful, nothing is returned. If validation is unsuccessful, an exception is thrown explaining the nature of the validation error. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|rule| <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule'>SoftLayer_Network_Firewall_Update_Request_Rule </a>| The rule to validate|
|applyToComponentId| integer| The ID of a SoftLayer_Network_Component_Firewall this rule will apply to.|
|applyToAclId| integer| The ID of a SoftLayer_Network_Firewall_Module_Context_Interface_AccessControlList this rule will apply to.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
void

