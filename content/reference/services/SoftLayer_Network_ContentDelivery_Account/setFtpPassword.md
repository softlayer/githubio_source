---
title: "setFtpPassword"
description: "With a CDN FTP, you can upload contents to CDN host server. Once you uploaded contents, your contents will be fetched by... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::setFtpPassword

Updates a CDN FTP user password


## Overview 
With a CDN FTP, you can upload contents to CDN host server. Once you uploaded contents, your contents will be fetched by the CDN POP (Points of Presence) servers as needed. 

CDN supports three protocols: Flash streaming (rtmp), Window Media streaming (mms) and HTTP. Once you log in to the CDN FTP server, you will see three directories under /media directory.  You have to upload your contents to a proper directory to use the different services. Refer to [[SoftLayer_Network_ContentDelivery_Account|CDN Account]] service overview for details on the CDN FTP server. "gzip" is supported if you compress your content before uploading and you have to change its extension to ".gz".  [SoftLayer_Network_ContentDelivery_Account::createOriginPullRule|Origin Pull] also supports "gzip" contents and you don't have to modify file extension with Origin Pull. Once uploaded, your contents should be available almost immediately to visitors.  However, it may take about 30 minutes to propagate files to the entire CDN network after uploading. For more details, visit our [hhttp://knowledgelayer.softlayer.com/topic/cdn KnowledgeLayer] 

This method updates the password for your CDN FTP account on the ftp.cdnlayer.service.softlayer.com server. You must provide an alphanumeric value for a new password.  - _ ! % # $ ^ & * characters are allowed beside an alphanumeric string. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newPassword| string| New password|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::createFtpUser](/reference/services/SoftLayer_Network_ContentDelivery_Account/createFtpUser )
*  [SoftLayer_Network_ContentDelivery_Account::getFtpAttributes](/reference/services/SoftLayer_Network_ContentDelivery_Account/getFtpAttributes )

