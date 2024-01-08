---
title: "approveChanges"
description: "When a change is made to an upgrade by Sales, this method will approve the changes that were made. A customer must acknowledge the change and approve it so that the upgrade request can proceed. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Upgrade_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Upgrade_Request"
---

### [REST Example](#approveChanges-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#approveChanges-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Upgrade_Request/{SoftLayer_Product_Upgrade_RequestID}/approveChanges'
```
