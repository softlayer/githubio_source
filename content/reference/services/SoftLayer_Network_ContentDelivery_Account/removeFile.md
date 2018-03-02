---
title: "removeFile"
description: "With this method you can remove a file or a directory on the CDN FTP server. If a source name ends with a slash (/), thi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::removeFile
## Overview 
With this method you can remove a file or a directory on the CDN FTP server. If a source name ends with a slash (/), this method assumes it is a directory.  A source name must be an absolute path. It does not check to see if a file or directory exists before deletion. You can only remove files and directories that are in /media folder. Be sure to catch an exception for the detail on an error. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|source| string| absolute path of a file or a directory name|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean

