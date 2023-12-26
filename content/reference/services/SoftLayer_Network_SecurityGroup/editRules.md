---
title: "editRules"
description: "Edit rules that belong to the security group. An array of skeleton [SoftLayer_Network_SecurityGroup_Rule](/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule) objects must be sent in with only the properties defined that you want to change. To edit a property to null, send in -1 for integer properties and '' for string properties. Unchanged properties are left alone. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_SecurityGroup"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_SecurityGroup_Rule]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/{SoftLayer_Network_SecurityGroupID}/editRules'
```
