---
title: "getObject"
description: "getObject retrieves the SoftLayer_Software_VirtualLicense object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Software_VirtualLicense service. You can only retrieve Virtual Licenses assigned to your account number. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_VirtualLicense"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_VirtualLicense"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_VirtualLicense/{SoftLayer_Software_VirtualLicenseID}/getObject'
```
