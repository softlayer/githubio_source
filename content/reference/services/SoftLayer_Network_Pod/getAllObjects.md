---
title: "getAllObjects"
description: "Filtering is supported for ``datacenterName`` and ``capabilities``. When filtering on capabilities, use the ``in`` opera... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Pod"
aliases:
    - "/reference/services/softlayer_network_pod/getAllObjects"
---
# [SoftLayer_Network_Pod](/reference/services/SoftLayer_Network_Pod)::getAllObjects

Retrieve a list of Pods; optionally filtered via datacenter and/or capabilities.


## Overview 
Filtering is supported for ``datacenterName`` and ``capabilities``. When filtering on capabilities, use the ``in`` operation. Pods fulfilling all capabilities provided will be returned. ``datacenterName`` represents an operation against ``SoftLayer_Location_Datacenter.name`, such as dal05 when referring to Dallas 5. 

```Examples:``` 

List Pods in a specific datacenter. <pre> datacenterName.operation = 'dal06' </pre> 

List Pods in a geographical area. <pre> datacenterName.operation = '^= dal' </pre> 

List Pods in a region fulfilling capabilities. <pre> datacenterName.operation = '^= dal' capabilities.operation = 'in' capabilities.options = [ { name = data, value = [SOME_CAPABILITY, ANOTHER_CAPABILITY] } ] </pre> 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_PodObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Network_PodObjectFilter

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Pod'>SoftLayer_Network_Pod[] </a>

