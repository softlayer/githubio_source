---
title: "getFileList"
description: "This method returns a collection of the file objects within a container and the given path."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Hub_Swift_Share"
---
# SoftLayer_Network_Storage_Hub_Swift_Share::getFileList
## Overview 
This method returns a collection of the file objects within a container and the given path. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|container| string| Name of a container|
|path| string| The file name, this could contain '/'s to denote a pseudo directory structure|


### Required Headers
* authenticate

### Optional Headers
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity'>SoftLayer_Container_Utility_File_Entity[] </a>

