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
aliases:
    - "/reference/services/softlayer_network_securitygroup/deleteObject"
---
# [SoftLayer_Network_SecurityGroup](/reference/services/SoftLayer_Network_SecurityGroup)::deleteObject


Delete a security group.


## Overview 
Delete a security group for an account. A security group cannot be deleted if any network components are attached or if the security group is a remote security group for a [SoftLayer_Network_SecurityGroup_Rule]({{<ref "reference/datatypes/SoftLayer_Network_SecurityGroup_Rule">}}). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_SecurityGroupInitParameters


### Return Values
* boolean




