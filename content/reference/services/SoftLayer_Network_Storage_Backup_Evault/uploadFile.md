---
title: "uploadFile"
description: "{{CloudLayerOnlyMethod}} Upload a file to a Storage account's root directory. Once uploaded, this method returns new fil... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/uploadFile"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::uploadFile

Upload a file to a Storage account's root directory.


## Overview 
{{CloudLayerOnlyMethod}} Upload a file to a Storage account's root directory. Once uploaded, this method returns new file entity identifier for the upload file. 

The following properties are required in the ''file'' parameter. 
*'''name''': The name of the file you wish to upload
*'''content''': The raw contents of the file you wish to upload.
*'''contentType''': The MIME-type of content that you wish to upload.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|file| <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>| The file you wish to upload.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>

### External Links


* [MIME Media Types at iana.org](http://www.iana.org/assignments/media-types/)



### Associated Methods

*  [SoftLayer_Network_Storage::downloadFile](/reference/services/SoftLayer_Network_Storage/downloadFile )



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



