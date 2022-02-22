---
title: "getCloudObjectStorageMetrics"
description: "Makes a request to Cloud Object Storage metricsAPI service and when successful, returns an associative array with two elements: 

if 200: 

[ <response Status Code String>, <JSON from metricsAPI as outlined below as String> ] 

if  not 200: 

[ <response Status Code String>, <response body as String> ] 



{ 'start': '<timeInMilliseconds>', 'errors': [], 'end': '<timeInMilliseconds>', 'resource_type': 'account', 'warnings': [], 'resources': [{'metrics' : [{'name': 'retrieval', 'value': '<number>'}]}] } 

Notes: 1) When no data is found for a particular triplet (resource_id, storage_location, storage_class) a JSON element is inserted to the warnings Array. 2) If all queried triplets find data, only the resources Array will be populated, errors and warnings will remain empty. 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Hub_Cleversafe_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Storage_Hub_Cleversafe_Account"
---
