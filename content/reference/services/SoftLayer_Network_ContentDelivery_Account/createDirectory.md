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
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/createDirectory"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::createDirectory

Creates a directory on the CDN FTP server


## Overview 
You can further organize your contents on the CDN FTP server by creating sub directories.  This method creates a directory on the CDN FTP server. A user must have CDN_FILE_MANAGE privilege to use this method. A directory name must be an absolute path and you can only create sub directories in /media folder. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|directoryName| string| absolute path of a new directory name|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws an exception if a user does not have CDN_FILE_MANAGE privilege. 

* SoftLayer_Exception_Public 

> Throws an exception if a directory name is empty. 

* SoftLayer_Exception_Public 

> Throws an exception if a user attempts to create a directory outside of /media folder. 



