---
title: "getSurveyRequiredFlag"
description: "Whether or not a user must take a brief survey the next time they log into the SoftLayer customer portal."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

### [REST Example](#getSurveyRequiredFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSurveyRequiredFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/getSurveyRequiredFlag'
```
