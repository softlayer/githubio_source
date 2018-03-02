---
title: "detachNetworkComponents"
description: "Detach virtual guest network components from a security group by deleting its [[SoftLayer_Virtual_Network_SecurityGroup_... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
---
# SoftLayer_Network_SecurityGroup::detachNetworkComponents
## Overview 
Detach virtual guest network components from a security group by deleting its [[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding (type)]]. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkComponentIds| array of integers| An array of SoftLayer_Virtual_Guest_Network_Component IDs for components you want to detach|


### Required Headers
* authenticate
* SoftLayer_Network_SecurityGroupInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Request'>SoftLayer_Network_SecurityGroup_Request </a>

