---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_ContentDelivery_Authentication_Address object whose ID number corresponds to t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Address"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_authentication_address/getObject"
---
# [SoftLayer_Network_ContentDelivery_Authentication_Address](/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address)::getObject

Retrieve a SoftLayer_Network_ContentDelivery_Authentication_Address record.


## Overview 
getObject retrieves the SoftLayer_Network_ContentDelivery_Authentication_Address object whose ID number corresponds to the ID number of the initial parameter passed to the SoftLayer_Network_ContentDelivery_Authentication_Address service. You can only retrieve authentication IP addresses assigned to one of your CDN account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_ContentDelivery_Authentication_AddressInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_ContentDelivery_Authentication_AddressObjectMask
* SoftLayer_Network_ContentDelivery_Authentication_AddressObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Address'>SoftLayer_Network_ContentDelivery_Authentication_Address </a>




