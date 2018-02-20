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
---
# SoftLayer_Network_Storage_Iscsi::downloadFile
## Overview 
{{CloudLayerOnlyMethod}} Download a file from a Storage account. This method returns a file's details including the file's raw content. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fileId| string| The id or guid of the file you wish to download.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_IscsiInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>
