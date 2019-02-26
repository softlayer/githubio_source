---
title: "getGraph"
description: "{{CloudLayerOnlyMethod}} 

getGraph() retrieves a Storage account's usage and returns a PNG graph image, title, and the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/getGraph"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::getGraph

Retrieve a graph representing the bandwidth used by a Storage account.


## Overview 
{{CloudLayerOnlyMethod}} 

getGraph() retrieves a Storage account's usage and returns a PNG graph image, title, and the minimum and maximum dates included in the graphed date range. Virtual Server storage accounts can also graph upload and download bandwidth usage. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| The starting date of the range of data you wish to collect.|
|endDate| dateTime| The ending date of the range of data you wish to collect.|
|type| string| The type of data you wish to graph. Either "usage", "upload", "download" or "bandwidth".|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Backup_EvaultInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Not yet implemented for this Storage type." if the Storage type is not supported. 



