---
title: "downloadFile"
description: "{{CloudLayerOnlyMethod}} Download a file from a Storage account. This method returns a file's details including the file... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
aliases:
    - "/reference/services/softlayer_network_storage_iscsi/downloadFile"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::downloadFile

Download a file from a Storage account.


## Overview 
{{CloudLayerOnlyMethod}} Download a file from a Storage account. This method returns a file's details including the file's raw content. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileId| string| The id or guid of the file you wish to download.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>


### Associated Methods

*  [SoftLayer_Network_Storage::uploadFile](/reference/services/SoftLayer_Network_Storage/uploadFile )
*  [SoftLayer_Network_Storage::getFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getFileByIdentifier )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



