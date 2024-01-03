---
title: "enroll"
description: "Create a new Service Provider Enrollment "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest"
---

# [REST Example](#enroll-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#enroll-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest/enroll'
```
