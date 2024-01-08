---
title: "getCustomerCountryLocationRestrictions"
description: "This references relationship between brands, locations and countries associated with a user's account that are ineligible when ordering products. For example, the India datacenter may not be available on this brand for customers that live in Great Britain."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
type: "reference"
layout: "method"
mainService : "SoftLayer_Brand"
---

### [REST Example](#getCustomerCountryLocationRestrictions-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCustomerCountryLocationRestrictions-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/{SoftLayer_BrandID}/getCustomerCountryLocationRestrictions'
```
