---
title: "createFtpUser"
description: "This method allows you to create a default CDN FTP user record on the ftp.cdnlayer.service.softlayer.com server. As with... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::createFtpUser
## Overview 
This method allows you to create a default CDN FTP user record on the ftp.cdnlayer.service.softlayer.com server. As with a CDN FTP user account, you can upload contents to the CDN host server through the SoftLayer private network.  SoftLayer currently allows only one FTP user for each CDN account. Your default CDN FTP user record is created upon successful creation of a CDN account.  You may not need to use this method at all. This is provided in support of the previous CDN customers. SoftLayer may offer multiple CDN FTP users for a single CDN account in the future. 

Optionally, you can provide a new password when invoking this method and a new password must follow the rules below: 
* ...must be between 8 and 20 characters long
* ...must be an alphanumeric value
* ...can contain these characters: - _ ! % # $ ^ & *

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newPassword| string| If a new password was not provided, it will be auto-generated|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean
