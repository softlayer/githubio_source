---
title: "getDirectoryInformation"
description: "This method returns a collection of SoftLayer_Container_Network_Ftp_Directory objects. You can retrieve directory inform... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
aliases:
    - "/reference/services/softlayer_network_media_transcode_account/getDirectoryInformation"
---
# [SoftLayer_Network_Media_Transcode_Account](/reference/services/SoftLayer_Network_Media_Transcode_Account)::getDirectoryInformation

Returns a directory listing


## Overview 
This method returns a collection of SoftLayer_Container_Network_Ftp_Directory objects. You can retrieve directory information for /in and /out directories. A [[SoftLayer_Container_Network_Directory_Listing|Directory Listing]] object contains a type (indicating whether it is a file or a directory), name and file count if it is a directory. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|directoryName| string| comma separated Extensions to restrict results to|
|extensionFilter| string| A directory name|


### Required Headers
* authenticate
* SoftLayer_Network_Media_Transcode_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Directory_Listing'>SoftLayer_Container_Network_Directory_Listing[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception if connection to the Transcode FTP server fails 

* SoftLayer_Exception_Public 

> Throw the exception if it fails to login to the Transcode FTP server fails 

* SoftLayer_Exception_Public 

> Throw the exception if a directory doesn't exist on the Transcode FTP server 



