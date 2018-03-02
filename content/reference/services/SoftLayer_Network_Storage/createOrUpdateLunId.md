---
title: "createOrUpdateLunId"
description: "The LUN ID only takes effect during the Host Authorization process. It is required to de-authorize all hosts before usin... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage"
---
# SoftLayer_Network_Storage::createOrUpdateLunId
## Overview 
The LUN ID only takes effect during the Host Authorization process. It is required to de-authorize all hosts before using this method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|lunId| integer| <<< EOT|


### Required Headers
* authenticate
* SoftLayer_Network_StorageInitParameters

### Optional Headers
* SoftLayer_Network_StorageObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage_Property'>SoftLayer_Network_Storage_Property </a>

