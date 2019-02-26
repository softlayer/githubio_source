---
title: "createOriginPullRule"
description: "This method is deprecated, please use [[[[SoftLayer_Network_ContentDelivery_Account::createOriginPullMapping|createOrigi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/createOriginPullRule"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::createOriginPullRule

Sets up an Origin Pull domain rule


## Overview 
This method is deprecated, please use [[[[SoftLayer_Network_ContentDelivery_Account::createOriginPullMapping|createOriginPullMapping]] method instead. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|originDomain| string| Specify a host name for your Origin Pull|
|cnameRecord| string| Specify a CNAME record that points to your CDN host|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_ACCOUNT_MANAGE privilege. 

* SoftLayer_Exception_Public 

> Throws an exception if an Origin Pull domain name is not provided. 

* SoftLayer_Exception_Public 

> Throws an exception if an Origin Pull rule is already set up. 

* SoftLayer_Exception_Public 

> Throws an exception if a connection to the CDN FTP server failed. 

* SoftLayer_Exception_Public 

> Throws an exception if nslookup failed on an Origin Pull domain. 

* SoftLayer_Exception_Public 

> Throws an exception if a CNAME is provided and nslookup failed on CNAME record. 

* SoftLayer_Exception_Public 

> Throws an exception if a CNAME is provided and CNAME does not point to "<CDN_AcccountName>.http.cdn.softlayer.net.". 



