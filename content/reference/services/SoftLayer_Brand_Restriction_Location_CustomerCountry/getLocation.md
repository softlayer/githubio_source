---
title: "getLocation"
description: "This references the datacenter that has a brand-location-country restriction setup. For example, if a datacenter is listed with a restriction for Canada, a Canadian customer may not be eligible to order services at that location."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand_Restriction_Location_CustomerCountry"
type: "reference"
layout: "method"
mainService : "SoftLayer_Brand_Restriction_Location_CustomerCountry"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand_Restriction_Location_CustomerCountry/{SoftLayer_Brand_Restriction_Location_CustomerCountryID}/getLocation'
```
