---
title: "getCurrentBenchmarkCertificationResultFile"
description: "Attempt to retrieve the file associated with the current benchmark certification result, if such a file exists.  If ther... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getCurrentBenchmarkCertificationResultFile"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getCurrentBenchmarkCertificationResultFile

Get the file for the current benchmark certification result, if it exists.


## Overview 
Attempt to retrieve the file associated with the current benchmark certification result, if such a file exists.  If there is no file for this benchmark certification result, calling this method throws an exception. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* binary data



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'This hardware currently does not have a benchmark certification.' when a benchmark certification test has not been performed for this hardware. 



