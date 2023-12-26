---
title: "getLicenseFile"
description: "Attempt to retrieve the file associated with a virtual license, if such a file exists.  If there is no file for this virtual license, calling this method will either throw an exception or return false. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_VirtualLicense/{SoftLayer_Software_VirtualLicenseID}/getLicenseFile'
```
