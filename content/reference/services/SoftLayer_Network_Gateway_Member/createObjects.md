---
title: "createObjects"
description: "Create multiple new hardware members on the gateway. This also asynchronously sets up the network for the members. Progr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Member"
aliases:
    - "/reference/services/softlayer_network_gateway_member/createObjects"
---
# [SoftLayer_Network_Gateway_Member](/reference/services/SoftLayer_Network_Gateway_Member)::createObjects


Add a member to a gateway


## Overview 
Create multiple new hardware members on the gateway. This also asynchronously sets up the network for the members. Progress of this process can be monitored via the gateway status. All members created with this object must have no VLANs attached. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member[] </a>| An array of SoftLayer_Network_Gateway_Member objects that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Gateway_MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member[] </a>




