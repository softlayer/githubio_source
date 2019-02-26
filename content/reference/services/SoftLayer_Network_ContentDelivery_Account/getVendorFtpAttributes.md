---
title: "getVendorFtpAttributes"
description: "This method returns your login credentials to the public CDN FTP."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/getVendorFtpAttributes"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::getVendorFtpAttributes

Returns login credentials to CDN FTP server


## Overview 
This method returns your login credentials to the public CDN FTP. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Authentication_Data'>SoftLayer_Container_Network_Authentication_Data </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_FILE_MANAGE privilege. 

* SoftLayer_Exception_Public 

> Throws an exception if a CDN account is disabled. 



