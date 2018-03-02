---
title: "collectBandwidth"
description: "{{CloudLayerOnlyMethod}} 

collectBandwidth() Retrieve the bandwidth usage for the current billing cycle."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
---
# SoftLayer_Network_Storage_Backup_Evault::collectBandwidth
## Overview 
{{CloudLayerOnlyMethod}} 

collectBandwidth() Retrieve the bandwidth usage for the current billing cycle. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|type| string| The bandwidth type to collect usage for (upload, download)|
|startDate| dateTime| The starting date of the range of data you wish to collect.|
|endDate| dateTime| The ending date of the range of data you wish to collect.|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters

### Optional Headers

### Return Values
unsigned long

