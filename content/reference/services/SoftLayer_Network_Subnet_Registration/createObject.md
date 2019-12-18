---
title: "createObject"
description: "Create registration with a global registrar to associate an assigned subnet with the provided contact details. 

Contact... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
aliases:
    - "/reference/services/softlayer_network_subnet_registration/createObject"
---
# [SoftLayer_Network_Subnet_Registration](/reference/services/SoftLayer_Network_Subnet_Registration)::createObject

Create a new subnet registration


## Overview 
Create registration with a global registrar to associate an assigned subnet with the provided contact details. 

Contact information is provided in the form of a [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}). 

The same applies to [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}), though these references need not be provided. The system will create a reference to the network described by the registration's subnet in the absence of a provided network detail reference. However, if a specific detail is referenced, it must describe the same subnet as the registration. 

A template containing the following properties will create a subnet registration: 


* networkIdentifier
* cidr
* detailReferences


``networkIdentifier`` is the base address of the public, SoftLayer owned subnet which is being registered. ``cidr`` must be an integer representing the CIDR of the subnet to be registered. The ``networkIdentifier``/``cidr`` must represent an assigned subnet. ``detailReferences`` tie the registration to SoftLayer_Account_Regional_Registry_Detail objects. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration </a>| The SoftLayer_Network_Subnet_Registration object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Subnet_RegistrationObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration </a>


### Associated Methods

*  [SoftLayer_Network_Subnet_Registration::createObjects](/reference/services/SoftLayer_Network_Subnet_Registration/createObjects )
*  [SoftLayer_Account_Regional_Registry_Detail::createObject](/reference/services/SoftLayer_Account_Regional_Registry_Detail/createObject )



### Error Handling

* SoftLayer_Exception_AlreadyExists 

> <<< EOT 

* SoftLayer_Exception_NotSupported 

> <<< EOT 

* SoftLayer_Exception_InvalidValue 

> <<< EOT 

* SoftLayer_Exception_NotFound 

> <<< EOT 



