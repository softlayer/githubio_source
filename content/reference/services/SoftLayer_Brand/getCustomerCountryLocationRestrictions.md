---
title: "getCustomerCountryLocationRestrictions"
description: "Retrieve this references relationship between brands, locations and countries associated with a user's account that are... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
aliases:
    - "/reference/services/softlayer_brand/getCustomerCountryLocationRestrictions"
---
# [SoftLayer_Brand](/reference/services/SoftLayer_Brand)::getCustomerCountryLocationRestrictions

Retrieve this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.


## Overview 
Retrieve this references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_BrandInitParameters
* authenticate


### Optional Headers
* SoftLayer_BrandObjectMask
* SoftLayer_BrandObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Brand_Restriction_Location_CustomerCountry'>SoftLayer_Brand_Restriction_Location_CustomerCountry[] </a>




