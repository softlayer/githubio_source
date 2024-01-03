---
title: "getProvisionState"
description: "The getProvisionState method retrieves the provision state of the resource. The provision state may be used to determine when it is considered safe to perform additional setup operations. The method returns 'PROCESSING' to indicate the provision is in progress and 'COMPLETE' when the provision is complete. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
type: "reference"
layout: "method"
mainService : "SoftLayer_Resource_Metadata"
---

# [REST Example](#getProvisionState-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getProvisionState-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getProvisionState'
```
