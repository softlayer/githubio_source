---
title: "getAllFilesByFilter"
description: "{{CloudLayerOnlyMethod}} Retrieve details such as id, name, size, create date for all files matching the filter's criter... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# [SoftLayer_Network_Storage_Iscsi](/reference/services/SoftLayer_Network_Storage_Iscsi)::getAllFilesByFilter

Retrieve a listing of all files matching the filter's criteria in a Storage account's root directory.


## Overview 
{{CloudLayerOnlyMethod}} Retrieve details such as id, name, size, create date for all files matching the filter's criteria in a Storage account's root directory. This does not download file content. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|filter| <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>| A filter to search for remote files by.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity[] </a>

