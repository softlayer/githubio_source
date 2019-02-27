---
title: "deleteOriginPullRule"
description: "This method removes an Origin Pull domain rule.  Once an Origin Pull rule is removed, you will be able to access the /me... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/deleteOriginPullRule"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::deleteOriginPullRule

Removes an Origin Pull domain rule


## Overview 
This method removes an Origin Pull domain rule.  Once an Origin Pull rule is removed, you will be able to access the /media/http directory. It will take 10 to 15 minutes for this to take effect after you remove your Origin Pull rule.  Cached contents on CDN POPs may live longer than 15 minutes. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|originMappingId| string| An origin pull mapping ID|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_ContentDelivery_Account::createOriginPullRule](/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullRule )



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_ACCOUNT_MANAGE privilege. 

* SoftLayer_Exception_Public 

> Throws an exception if a connection to the CDN FTP server failed. 

* SoftLayer_Exception_Public 

> Throws an exception if an Origin Pull rule is not set up. 



