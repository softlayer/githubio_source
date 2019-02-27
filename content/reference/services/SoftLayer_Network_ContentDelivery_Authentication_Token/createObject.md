---
title: "createObject"
description: "This method is deprecated! Use the [[SoftLayer_Network_ContentDelivery_Authentication_Token::getTimedToken|getTimedToken... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Token"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_authentication_token/createObject"
---
# [SoftLayer_Network_ContentDelivery_Authentication_Token](/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token)::createObject

(DEPRECATED) Creates a managed authentication token


## Overview 
This method is deprecated! Use the [[SoftLayer_Network_ContentDelivery_Authentication_Token::getTimedToken|getTimedToken]] method. 

This method creates a managed authentication token. When passing a parameter, the only required value is your CDN account id which can be obtained from the [[SoftLayer_Account::getCdnAccounts|getCdnAccounts]] method. There are 3 optional parameters you can pass: 


* name - This helps you keep track of managed tokens.
* referrer - If set, the token validation will check the client's referrer. Keep in mind, if a client doesn't have the referrer information, the token validation will fail.
* clientIp - If set, the token validation will check the client's IP address.



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Token'>SoftLayer_Network_ContentDelivery_Authentication_Token </a>| The SoftLayer_Network_ContentDelivery_Authentication_Token object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_ContentDelivery_Authentication_TokenObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Token'>SoftLayer_Network_ContentDelivery_Authentication_Token </a>




