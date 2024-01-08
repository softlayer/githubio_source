---
title: "setTags"
description: "Tag a subnet by passing in one or more tags separated by a comma. Any existing tags you wish to keep should be included in the set of tags, as any missing tags will be removed. To remove all tags from the subnet, send an empty string. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet"
---

### [REST Example](#setTags-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setTags-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/setTags'
```
