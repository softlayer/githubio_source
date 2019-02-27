---
title: "addRules"
description: "Add new rules to a security group by sending in an array of template [[SoftLayer_Network_SecurityGroup_Rule (type)]] obj... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
aliases:
    - "/reference/services/softlayer_network_securitygroup/addRules"
---
# [SoftLayer_Network_SecurityGroup](/reference/services/SoftLayer_Network_SecurityGroup)::addRules

Add new rules to a security group.


## Overview 
Add new rules to a security group by sending in an array of template [[SoftLayer_Network_SecurityGroup_Rule (type)]] objects to be created. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ruleTemplates| <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule'>SoftLayer_Network_SecurityGroup_Rule[] </a>| An array of rule objects you want to create|


### Required Headers
* authenticate
* SoftLayer_Network_SecurityGroupInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_RequestRules'>SoftLayer_Network_SecurityGroup_RequestRules </a>




