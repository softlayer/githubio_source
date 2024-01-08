---
title: "getCountriesAndStates"
description: "This method will return a collection of [SoftLayer_Container_Collection_Locale_CountryCode](/reference/datatypes/SoftLayer_Container_Collection_Locale_CountryCode) objects. If the country has states, a [SoftLayer_Container_Collection_Locale_StateCode](/reference/datatypes/SoftLayer_Container_Collection_Locale_StateCode) collection will be provided with the country. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Locale"
classes:
    - "SoftLayer_Locale_Country"
type: "reference"
layout: "method"
mainService : "SoftLayer_Locale_Country"
---

### [REST Example](#getCountriesAndStates-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCountriesAndStates-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Locale_Country/getCountriesAndStates'
```
