---
title: "createObject"
description: "This method creates an authentication IP record.  Required parameters are 


* cdnAccountId - A CDN account id that belo... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Address"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_authentication_address/createObject"
---
# [SoftLayer_Network_ContentDelivery_Authentication_Address](/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Address)::createObject

Creates an authentication IP record


## Overview 
This method creates an authentication IP record.  Required parameters are 


* cdnAccountId - A CDN account id that belongs to your SoftLayer Account
* ipAddress - An IP address or a IP range
* accessType- It can be "ALLOW" or "DENY"

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Address'>SoftLayer_Network_ContentDelivery_Authentication_Address </a>| The SoftLayer_Network_ContentDelivery_Authentication_Address object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_ContentDelivery_Authentication_AddressObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Address'>SoftLayer_Network_ContentDelivery_Authentication_Address </a>




