---
title: "getVatCountries"
description: "This method will return an array of ISO 3166 Alpha-2 country codes that use a Value-Added Tax (VAT) ID. Note the difference between [SoftLayer_Locale_Country::getVatRequiredCountryCodes](/reference/services/SoftLayer_Locale_Country/getVatRequiredCountryCodes) - this method will provide <strong>all</strong> country codes that use VAT ID, including those which are required. "
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

# [REST Example](#getVatCountries-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getVatCountries-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Locale_Country/getVatCountries'
```
