---
title: "attachNetworkComponents"
description: "Attach virtual guest network components to a security group by creating [[SoftLayer_Virtual_Network_SecurityGroup_Networ... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
---
# SoftLayer_Network_SecurityGroup::attachNetworkComponents
## Overview 
Attach virtual guest network components to a security group by creating [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)]] objects. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkComponentIds| array of integers| An array of SoftLayer_Virtual_Guest_Network_Component IDs for components you want to attach|


### Required Headers
* authenticate
* SoftLayer_Network_SecurityGroupInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Request'>SoftLayer_Network_SecurityGroup_Request </a>
