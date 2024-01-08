---
title: "getLicenseFile"
description: "Attempt to retrieve the file associated with a software component.  If the software component does not support downloading license files an exception will be thrown. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component"
---

### [REST Example](#getLicenseFile-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLicenseFile-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component/{SoftLayer_Software_ComponentID}/getLicenseFile'
```
