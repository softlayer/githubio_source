---
title: "getBrandCountryRestrictions"
description: "Retrieve this references relationship between brands, locations and countries associated with a user's account that are... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
aliases:
    - "/reference/services/softlayer_location_datacenter/getBrandCountryRestrictions"
---
# [SoftLayer_Location_Datacenter](/reference/services/SoftLayer_Location_Datacenter)::getBrandCountryRestrictions


Retrieve this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.


## Overview 
Retrieve this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Location_DatacenterInitParameters
* authenticate


### Optional Headers
* SoftLayer_Location_DatacenterObjectMask
* SoftLayer_Location_DatacenterObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry'>SoftLayer_Brand_Restriction_Location_CustomerCountry[] </a>




