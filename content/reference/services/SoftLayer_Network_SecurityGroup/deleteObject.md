---
title: "deleteObject"
description: "Delete a security group for an account. A security group cannot be deleted if any network components are attached or if... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
---
# SoftLayer_Network_SecurityGroup::deleteObject
## Overview 
Delete a security group for an account. A security group cannot be deleted if any network components are attached or if the security group is a remote security group for a [[SoftLayer_Network_SecurityGroup_Rule (type)|rule]]. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_SecurityGroupInitParameters

### Optional Headers

### Return Values
boolean

