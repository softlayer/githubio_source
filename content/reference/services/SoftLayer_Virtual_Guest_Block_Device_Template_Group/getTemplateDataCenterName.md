---
title: "getTemplateDataCenterName"
description: "This method allows you to grab the first data center that the image(s) reside on so we can pull it from there. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
---

### [REST Example](#getTemplateDataCenterName-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTemplateDataCenterName-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Block_Device_Template_Group/{SoftLayer_Virtual_Guest_Block_Device_Template_GroupID}/getTemplateDataCenterName'
```
