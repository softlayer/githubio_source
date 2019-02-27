---
title: "getOriginPullUrl"
description: "This method returns the domain name of your Origin Pull rule.  It assumes you have already setup an Origin Pull rule.  O... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getOriginPullUrl"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getOriginPullUrl

Gets Origin Pull domain information


## Overview 
This method returns the domain name of your Origin Pull rule.  It assumes you have already setup an Origin Pull rule.  Otherwise, it will throw an exception. A returning value is the value of the first parameter (origin pull domain) you provided to [[SoftLayer_Network_ContentDelivery_Account::createOriginPullRule|createOriginPullRule]] method. See Error Handling section below for possible errors. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* string


### Associated Methods

*  [SoftLayer_Network_ContentDelivery_Account::createOriginPullRule](/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullRule )



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_ACCOUNT_MANAGE privilege. 

* SoftLayer_Exception_Public 

> Throws an exception if an Origin Pull rule is not set up. 



