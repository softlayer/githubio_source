---
title: "getFileByIdentifier"
description: "{{CloudLayerOnlyMethod}} Retrieve details such as id, name, size, create date of a file within a Storage account. This d... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
aliases:
    - "/reference/services/softlayer_network_storage/getFileByIdentifier"
---
# [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage)::getFileByIdentifier

Retrieve an individual file's details.


## Overview 
{{CloudLayerOnlyMethod}} Retrieve details such as id, name, size, create date of a file within a Storage account. This does not download file content. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|identifier| string| The id or guid of the file you wish to retrieve.|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity </a>


### associatedMethods

*  [SoftLayer_Network_Storage::getAllFiles](/reference/services/SoftLayer_Network_Storage/getAllFiles )
*  [SoftLayer_Network_Storage::downloadFile](/reference/services/SoftLayer_Network_Storage/downloadFile )

