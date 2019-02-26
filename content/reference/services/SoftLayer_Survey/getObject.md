---
title: "getObject"
description: "getObject retrieves the SoftLayer_Survey object whose ID number corresponds to the ID number of the init parameter passe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Survey"
classes:
    - "SoftLayer_Survey"
aliases:
    - "/reference/services/softlayer_survey/getObject"
---
# [SoftLayer_Survey](/reference/services/SoftLayer_Survey)::getObject

Retrieve a SoftLayer_Survey record.


## Overview 
getObject retrieves the SoftLayer_Survey object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Survey service. You can only retrieve the survey that your portal user has taken. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_SurveyInitParameters
* authenticate


### Optional Headers
* SoftLayer_SurveyObjectMask
* SoftLayer_SurveyObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Survey'>SoftLayer_Survey </a>




