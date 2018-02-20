---
title: "deleteObjects"
description: "Delete security groups for an account. A security group cannot be deleted if any network components are attached or if t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
---
# SoftLayer_Network_SecurityGroup::deleteObjects
## Overview 
Delete security groups for an account. A security group cannot be deleted if any network components are attached or if the security group is a remote security group for a [[SoftLayer_Network_SecurityGroup_Rule (type)|rule]]. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup[] </a>| An array of skeleton SoftLayer_Network_SecurityGroup objects that you wish to delete. Each object in the array must have at least their id properties defined.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean
