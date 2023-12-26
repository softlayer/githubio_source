---
title: "modifyPreferences"
description: "Using this method, multiple [SoftLayer_Layout_Profile_Preference](/reference/datatypes/SoftLayer_Layout_Profile_Preference) objects may be updated at once. 

Refer to [[SoftLayer_Layout_Profile::modifyPreference()]] for more information. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_Layout_Profile_Customer"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Layout_Profile_Preference]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Layout_Profile_Customer/{SoftLayer_Layout_Profile_CustomerID}/modifyPreferences'
```
