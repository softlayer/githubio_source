---
title: "getObject"
description: "This method retrieves a monitoring agent configuration template group reference whose identifier corresponds to the valu... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference"
aliases:
    - "/reference/services/softlayer_monitoring_agent_configuration_template_group_reference/getObject"
---
# [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference)::getObject

Retrieve a SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference record.


## Overview 
This method retrieves a monitoring agent configuration template group reference whose identifier corresponds to the value provided in the initialization parameter passed to the SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Monitoring_Agent_Configuration_Template_Group_ReferenceInitParameters
* authenticate


### Optional Headers
* SoftLayer_Monitoring_Agent_Configuration_Template_Group_ReferenceObjectMask
* SoftLayer_Monitoring_Agent_Configuration_Template_Group_ReferenceObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference'>SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference </a>



### Error Handling

* SoftLayer_Exception_ObjectNotFound 

> Throws the error 'Unable to find object with id of {id}.' if the given initialization parameter has an invalid identifier. 



