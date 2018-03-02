---
title: "createDirectory"
description: "You can further organize your contents on the CDN FTP server by creating sub directories.  This method creates a directo... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::createDirectory
## Overview 
You can further organize your contents on the CDN FTP server by creating sub directories.  This method creates a directory on the CDN FTP server. A user must have CDN_FILE_MANAGE privilege to use this method. A directory name must be an absolute path and you can only create sub directories in /media folder. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|directoryName| string| absolute path of a new directory name|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean

