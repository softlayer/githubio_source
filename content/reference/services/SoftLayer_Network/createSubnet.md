---
title: "createSubnet"
description: "Creation of a Subnet is necessary prior to provisioning compute resources into a Network. In order to create a Subnet, b... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
aliases:
    - "/reference/services/softlayer_network/createSubnet"
---
# [SoftLayer_Network](/reference/services/SoftLayer_Network)::createSubnet

Add a Subnet to the Network.


## Overview 
Creation of a Subnet is necessary prior to provisioning compute resources into a Network. In order to create a Subnet, both a [[SoftLayer_Network_Subnet|Subnet]] and [[SoftLayer_Network_Pod|Pod]] must be specified. The Pod determines where the Subnet will be available for use by compute resources. 

Provide a Subnet template containing the following properties: 
* networkIdentifier
* cidr
The ``networkIdentifier`` must represent an IP address within that specified by the Network. The ``cidr`` must be an integer between 24 and 29, inclusive, and represent a subnet size smaller than the Network's. The ``networkIdentifier``/``cidr`` must represent a valid subnet specification. 

Provide a Pod template containing the following property: 
* name
The ``name`` must represent a valid Pod e.g. sjc01.pod02. See [[SoftLayer_Network_Pod (type)]] for more information. 

The following constraints apply to Subnet creation: 
* It must fit within the bounds of the Network.
* It must be no larger than /24 and no smaller than /29.
* Its size must not equal that of the Network. This implies that a fully
utilized Network will have a minimum of two Subnets. 
* The Pod must support the ability to create Networks by having the
SUPPORTS_CUSTOMER_DEFINED_NETWORK capability. See [[SoftLayer_Network_Pod/getCapabilities]]. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnet| <a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>| Subnet to be created within the Network.|
|pod| <a href='/reference/datatypes/SoftLayer_Network_Pod'>SoftLayer_Network_Pod </a>| Designates the Pod the Subnet will be available in.|


### Required Headers
* authenticate
* SoftLayer_NetworkInitParameters

### Optional Headers
* SoftLayer_NetworkObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>

