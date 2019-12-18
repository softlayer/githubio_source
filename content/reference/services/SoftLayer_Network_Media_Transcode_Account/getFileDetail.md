---
title: "getFileDetail"
description: "This method returns detailed information of a media file that resides in the Transcode FTP server. A [SoftLayer_Containe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
aliases:
    - "/reference/services/softlayer_network_media_transcode_account/getFileDetail"
---
# [SoftLayer_Network_Media_Transcode_Account](/reference/services/SoftLayer_Network_Media_Transcode_Account)::getFileDetail

Returns detailed information on a video or audio file


## Overview 
This method returns detailed information of a media file that resides in the Transcode FTP server. A [SoftLayer_Container_Network_Media_Information]({{<ref "reference/datatypes/SoftLayer_Container_Network_Media_Information">}}) object contains media details such as file size, media format, frame rate, aspect ratio and so on.  This information is merely for reference purposes. You should not rely on this data. Our library grabs small pieces of data from a media file to gather media details.  This information may not be available for some files. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|source| string| The name of a source file|


### Required Headers
* authenticate
* SoftLayer_Network_Media_Transcode_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Media_Information'>SoftLayer_Container_Network_Media_Information </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception if connection to the Transcode FTP server fails 

* SoftLayer_Exception_Public 

> Throw the exception if it fails to login to the Transcode FTP server fails 

* SoftLayer_Exception_Public 

> Throw the exception if a source file doesn't exist on the Transcode FTP server 



