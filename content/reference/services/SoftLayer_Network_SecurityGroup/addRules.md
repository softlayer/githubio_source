---
title: "addRules"
description: "Add new rules to a security group by sending in an array of template [SoftLayer_Network_SecurityGroup_Rule](/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule) objects to be created. "
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

### [REST Example](#addRules-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addRules-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_SecurityGroup_Rule]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_SecurityGroup/{SoftLayer_Network_SecurityGroupID}/addRules'
```
