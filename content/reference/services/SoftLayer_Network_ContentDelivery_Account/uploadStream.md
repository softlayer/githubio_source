---
title: "uploadStream"
description: "With this method, you can upload binary data to the CDN FTP server.  This method supports files up to 20 Mega Bytes. You... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::uploadStream

Uploads binary data to the CDN FTP server


## Overview 
With this method, you can upload binary data to the CDN FTP server.  This method supports files up to 20 Mega Bytes. You need to use the CDN FTP (ftp.cdnlayer.service.softlayer.com) to upload files larger than 20 MB.  This method takes [[SoftLayer_Container_Utility_File_Attachment]] a first parameter. A target name must be an absolute path and you can only upload a file to a directory that is in /media folder. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|source| <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Attachment'>SoftLayer_Container_Utility_File_Attachment </a>| A source file data|
|target| string| An absolute path of a target file or a directory|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean

