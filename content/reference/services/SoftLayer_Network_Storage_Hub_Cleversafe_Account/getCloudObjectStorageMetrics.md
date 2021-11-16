---
title: "getCloudObjectStorageMetrics"
description: "Makes a request to Cloud Object Storage metricsAPI service and when successful, returns an associative array with two el... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Hub_Cleversafe_Account"
aliases:
    - "/reference/services/softlayer_network_storage_hub_cleversafe_account/getCloudObjectStorageMetrics"
---
# [SoftLayer_Network_Storage_Hub_Cleversafe_Account](/reference/services/SoftLayer_Network_Storage_Hub_Cleversafe_Account)::getCloudObjectStorageMetrics





## Overview 
Makes a request to Cloud Object Storage metricsAPI service and when successful, returns an associative array with two elements: 

if 200: 

[ <response Status Code String>, <JSON from metricsAPI as outlined below as String> ] 

if  not 200: 

[ <response Status Code String>, <response body as String> ] 



{ "start": "<timeInMilliseconds>", "errors": [], "end": "<timeInMilliseconds>", "resource_type": "account", "warnings": [], "resources": [{"metrics" : [{"name": "retrieval", "value": "<number>"}]}] } 

Notes: 1) When no data is found for a particular triplet (resource_id, storage_location, storage_class) a JSON element is inserted to the warnings Array. 2) If all queried triplets find data, only the resources Array will be populated, errors and warnings will remain empty. 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|start| string| Start time in milliseconds|
|end| string| End time in milliseconds|
|storageLocation| string| The storage location to query (ex. us-south)|
|storageClass| string| A comma separated list of all storage classes to query (ex. vault,cold)|
|metrics| string| A comma sepparated list of all metrics to query (ex. retrieval,copy_count)|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Hub_Cleversafe_AccountInitParameters


### Return Values
* array of strings




