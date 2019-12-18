---
title: "editRegistrationAttachedDetails"
description: "This method modifies a single registration by modifying the current [SoftLayer_Network_Subnet_Registration_Details]({{<r... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
aliases:
    - "/reference/services/softlayer_network_subnet_registration/editRegistrationAttachedDetails"
---
# [SoftLayer_Network_Subnet_Registration](/reference/services/SoftLayer_Network_Subnet_Registration)::editRegistrationAttachedDetails

Modify the link between a [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) object and two [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) objects simultaneously. 


## Overview 
This method modifies a single registration by modifying the current [SoftLayer_Network_Subnet_Registration_Details]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration_Details">}}) objects that are linked to that registration. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|personObjectSkeleton| <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Details'>SoftLayer_Network_Subnet_Registration_Details </a>| |
|networkObjectSkeleton| <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Details'>SoftLayer_Network_Subnet_Registration_Details </a>| |


### Required Headers
* authenticate


### Return Values
* boolean




