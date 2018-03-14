---
title: "getFtpAttributes"
description: "This method returns your Transcode FTP login credentials to the transcode.service.softlayer.com server. 

The Transcode... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
aliases:
    - "/reference/services/softlayer_network_media_transcode_account/getFtpAttributes"
---
# [SoftLayer_Network_Media_Transcode_Account](/reference/services/SoftLayer_Network_Media_Transcode_Account)::getFtpAttributes

Returns Transcode FTP login credentials


## Overview 
This method returns your Transcode FTP login credentials to the transcode.service.softlayer.com server. 

The Transcode FTP server is available via the SoftLayer private network. There is no API method that you can upload a file to Transcode server so you need to use an FTP client. You will have /in and /out directories on the Transcode FTP server.  You will have read-write privileges for /in directory and read-only privilege for /out directory. All the files in both /in and /out directories will be deleted after 72 hours from the creation date. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Media_Transcode_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_Authentication_Data'>SoftLayer_Container_Network_Authentication_Data </a>

