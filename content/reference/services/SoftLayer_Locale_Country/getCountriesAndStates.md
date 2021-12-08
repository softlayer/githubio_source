---
title: "getCountriesAndStates"
description: "This method will return a collection of [SoftLayer_Container_Collection_Locale_CountryCode]({{<ref 'reference/datatypes/... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Locale"
classes:
    - "SoftLayer_Locale_Country"
aliases:
    - "/reference/services/softlayer_locale_country/getCountriesAndStates"
---
# [SoftLayer_Locale_Country](/reference/services/SoftLayer_Locale_Country)::getCountriesAndStates





## Overview 
This method will return a collection of [SoftLayer_Container_Collection_Locale_CountryCode]({{<ref "reference/datatypes/SoftLayer_Container_Collection_Locale_CountryCode">}}) objects. If the country has states, a [SoftLayer_Container_Collection_Locale_StateCode]({{<ref "reference/datatypes/SoftLayer_Container_Collection_Locale_StateCode">}}) collection will be provided with the country. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|usFirstFlag| boolean| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Collection_Locale_CountryCode'>SoftLayer_Container_Collection_Locale_CountryCode[] </a>




