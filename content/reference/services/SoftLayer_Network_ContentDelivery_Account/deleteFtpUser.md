---
title: "deleteFtpUser"
description: "This method deletes your FTP user record on the ftp.cdnlayer.service.softlayer.com server. Refer to the service overview... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/deleteFtpUser"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::deleteFtpUser

Deletes a CDN FTP user record


## Overview 
This method deletes your FTP user record on the ftp.cdnlayer.service.softlayer.com server. Refer to the service overview of [[SoftLayer_Network_ContentDelivery_Account::createFtpUser|createFtpUser]] method for more information on the CDN FTP server. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_ContentDelivery_Account::createFtpUser](/reference/services/SoftLayer_Network_ContentDelivery_Account/createFtpUser )



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_FILE_MANAGE privilege. 



