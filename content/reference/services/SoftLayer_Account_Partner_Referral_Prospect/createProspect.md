---
title: "createProspect"
description: "Create a new Referral Partner Prospect "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Partner_Referral_Prospect"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Partner_Referral_Prospect"
---

# [REST Example](#createProspect-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createProspect-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Referral_Partner_Prospect, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Partner_Referral_Prospect/createProspect'
```
