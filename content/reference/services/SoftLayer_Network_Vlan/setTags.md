---
title: "setTags"
description: "Tag a VLAN by passing in one or more tags separated by a comma. Tag references are cleared out every time this method is called. If your VLAN is already tagged you will need to pass the current tags along with any new ones. To remove all tag references pass an empty string. To remove one or more tags omit them from the tag list. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan"
---

### [REST Example](#setTags-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setTags-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/setTags'
```
