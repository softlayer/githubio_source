---
title: "getObject"
description: "getObject retrieves the SoftLayer_Hardware_Component_Partition_Template object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Hardware_Component_Partition_Template service. You can only retrieve the partition templates that your account created or the templates predefined by SoftLayer. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_Template"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Component_Partition_Template"
---

### [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Component_Partition_Template/{SoftLayer_Hardware_Component_Partition_TemplateID}/getObject'
```
