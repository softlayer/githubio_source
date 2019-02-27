---
title: "getObject"
description: "This method retrieves a monitoring agent whose identifier corresponds to the value provided in the initialization parame... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/getObject"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::getObject

Retrieve a SoftLayer_Monitoring_Agent record.


## Overview 
This method retrieves a monitoring agent whose identifier corresponds to the value provided in the initialization parameter passed to the SoftLayer_Monitoring_Agent service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Monitoring_AgentInitParameters
* authenticate


### Optional Headers
* SoftLayer_Monitoring_AgentObjectMask
* SoftLayer_Monitoring_AgentObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Monitoring_Agent'>SoftLayer_Monitoring_Agent </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throws the error 'Unable to find object with id of {id}.' if the given initialization parameter has an invalid identifier. 



