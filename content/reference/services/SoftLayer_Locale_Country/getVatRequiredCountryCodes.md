---
title: "getVatRequiredCountryCodes"
description: "This method will return an array of ISO 3166 Alpha-2 country codes that use a Value-Added Tax (VAT) ID. Note the difference between [SoftLayer_Locale_Country::getVatCountries](/reference/services/SoftLayer_Locale_Country/getVatCountries) - this method will provide country codes where a VAT ID is required for onboarding to IBM Cloud. "
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

# [REST Example](#getVatRequiredCountryCodes-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getVatRequiredCountryCodes-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Locale_Country/getVatRequiredCountryCodes'
```
