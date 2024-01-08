---
title: "modifyPreference"
description: "This method modifies an existing associated [SoftLayer_Layout_Profile_Preference](/reference/datatypes/SoftLayer_Layout_Profile_Preference) object. If the preference object being modified is a default value object, a new record is created to override the default value. 

Only preferences that are assigned to a profile may be updated. Attempts to update a non-existent preference object will result in an exception being thrown. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile"
type: "reference"
layout: "method"
mainService : "SoftLayer_Layout_Profile"
---

### [REST Example](#modifyPreference-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#modifyPreference-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Layout_Profile_Preference]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Layout_Profile/{SoftLayer_Layout_ProfileID}/modifyPreference'
```
