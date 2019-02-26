---
title: "getResultFile"
description: "Attempt to retrieve the file associated with a benchmark certification result, if such a file exists.  If there is no fi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Benchmark_Certification"
aliases:
    - "/reference/services/softlayer_hardware_benchmark_certification/getResultFile"
---
# [SoftLayer_Hardware_Benchmark_Certification](/reference/services/SoftLayer_Hardware_Benchmark_Certification)::getResultFile

Retrieve the file for a benchmark certification result, if is exists.


## Overview 
Attempt to retrieve the file associated with a benchmark certification result, if such a file exists.  If there is no file for this benchmark certification result, calling this method throws an exception. The "getResultFile" method attempts to retrieve the file associated with a benchmark certification result, if such a file exists. If no file exists for the benchmark certification, an exception is thrown. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_Benchmark_CertificationInitParameters


### Return Values
* binary data



### Error Handling

* SoftLayer_Exception_Public 

> "The benchmark certification result file you attempted to retrieve does not exist." 



