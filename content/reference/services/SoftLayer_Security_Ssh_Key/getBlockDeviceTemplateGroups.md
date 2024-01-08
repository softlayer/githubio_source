---
title: "getBlockDeviceTemplateGroups"
description: "The image template groups that are linked to an SSH key."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Ssh_Key"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Ssh_Key"
---

### [REST Example](#getBlockDeviceTemplateGroups-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getBlockDeviceTemplateGroups-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Ssh_Key/{SoftLayer_Security_Ssh_KeyID}/getBlockDeviceTemplateGroups'
```
