---
title: "createObject"
description: "Create a new hardware member on the gateway. This also asynchronously sets up the network for this member. Progress of t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Member"
---
# SoftLayer_Network_Gateway_Member::createObject
## Overview 
Create a new hardware member on the gateway. This also asynchronously sets up the network for this member. Progress of this process can be monitored via the gateway status. All members created with this object must have no VLANs attached. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member </a>| The SoftLayer_Network_Gateway_Member object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Gateway_MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member </a>
