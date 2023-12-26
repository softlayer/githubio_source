---
title: "getLicenseFile"
description: "Attempt to retrieve the file associated with a software component.  If the software component does not support downloading license files an exception will be thrown. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Trellix"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component_Trellix"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component_Trellix/{SoftLayer_Software_Component_TrellixID}/getLicenseFile'
```
