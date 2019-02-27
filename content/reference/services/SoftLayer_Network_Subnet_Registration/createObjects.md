---
title: "createObjects"
description: "Create registrations with respective registrars to associate multiple assigned subnets with the provided contact details... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
aliases:
    - "/reference/services/softlayer_network_subnet_registration/createObjects"
---
# [SoftLayer_Network_Subnet_Registration](/reference/services/SoftLayer_Network_Subnet_Registration)::createObjects

Create registrations for multiple subnets


## Overview 
Create registrations with respective registrars to associate multiple assigned subnets with the provided contact details. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration[] </a>| An array of SoftLayer_Network_Subnet_Registration objects that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Subnet_RegistrationObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration[] </a>


### Associated Methods

*  [SoftLayer_Network_Subnet_Registration::createObject](/reference/services/SoftLayer_Network_Subnet_Registration/createObject )




