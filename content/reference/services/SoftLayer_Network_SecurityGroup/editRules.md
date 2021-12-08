---
title: "editRules"
description: "Edit rules that belong to the security group. An array of skeleton [SoftLayer_Network_SecurityGroup_Rule]({{<ref 'refere... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
aliases:
    - "/reference/services/softlayer_network_securitygroup/editRules"
---
# [SoftLayer_Network_SecurityGroup](/reference/services/SoftLayer_Network_SecurityGroup)::editRules


Edit rules that belong to a security group.


## Overview 
Edit rules that belong to the security group. An array of skeleton [SoftLayer_Network_SecurityGroup_Rule]({{<ref "reference/datatypes/SoftLayer_Network_SecurityGroup_Rule">}}) objects must be sent in with only the properties defined that you want to change. To edit a property to null, send in -1 for integer properties and "" for string properties. Unchanged properties are left alone. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ruleTemplates| <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule'>SoftLayer_Network_SecurityGroup_Rule[] </a>| An array of rule objects|


### Required Headers
* authenticate
* SoftLayer_Network_SecurityGroupInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_RequestRules'>SoftLayer_Network_SecurityGroup_RequestRules </a>




