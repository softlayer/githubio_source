---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Customer_Subnet object whose ID number corresponds to the ID number of the ini... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Customer_Subnet"
aliases:
    - "/reference/services/softlayer_network_customer_subnet/getObject"
---
# [SoftLayer_Network_Customer_Subnet](/reference/services/SoftLayer_Network_Customer_Subnet)::getObject

Retrieve a SoftLayer_Network_Customer_Subnet record.


## Overview 
getObject retrieves the SoftLayer_Network_Customer_Subnet object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Customer_Subnet service. You can only retrieve the subnet whose account matches the account that your portal user is assigned to. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Customer_SubnetInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Customer_SubnetObjectMask
* SoftLayer_Network_Customer_SubnetObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet'>SoftLayer_Network_Customer_Subnet </a>

