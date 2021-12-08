---
title: "attachNetworkComponents"
description: "Attach virtual guest network components to a security group by creating [SoftLayer_Virtual_Network_SecurityGroup_Network... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
aliases:
    - "/reference/services/softlayer_network_securitygroup/attachNetworkComponents"
---
# [SoftLayer_Network_SecurityGroup](/reference/services/SoftLayer_Network_SecurityGroup)::attachNetworkComponents


Attach network components to a security group by creating a network component binding. 


## Overview 
Attach virtual guest network components to a security group by creating [SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding]({{<ref "reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding">}}) objects. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkComponentIds| array of integers| An array of SoftLayer_Virtual_Guest_Network_Component IDs for components you want to attach|


### Required Headers
* authenticate
* SoftLayer_Network_SecurityGroupInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Request'>SoftLayer_Network_SecurityGroup_Request </a>




