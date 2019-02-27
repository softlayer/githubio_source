---
title: "createSwipTransaction"
description: "This function is used to create a new SoftLayer SWIP transaction to register your RWHOIS data with ARIN. SWIP transactio... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
aliases:
    - "/reference/services/softlayer_network_subnet/createSwipTransaction"
---
# [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet)::createSwipTransaction

create a SWIP transaction for a subnet


## Overview 
This function is used to create a new SoftLayer SWIP transaction to register your RWHOIS data with ARIN. SWIP transactions can only be initiated on subnets that contain more than 8 IP addresses. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_SubnetInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_PrivateSubnet 

> Exception thrown if a SWIP is attempted on a private network subnet. 

* SoftLayer_Exception_SubnetTooSmall 

> Exception thrown if a SWIP is attempted on a subnet smaller than 8 IP addresses. 

* SoftLayer_Exception_PreexistingTransaction 

> Exception thrown if a SWIP is attempted on a subnet that already has a SWIP transaction in progress. 

* SoftLayer_Exception_Network_Subnet_Registration 

> Exception thrown if an active registration already exists 



