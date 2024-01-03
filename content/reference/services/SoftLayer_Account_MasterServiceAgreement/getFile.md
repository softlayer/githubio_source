---
title: "getFile"
description: "Gets a File Entity container with the user's account's current MSA PDF. Gets a translation if one is available. Otherwise, gets the master document. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_MasterServiceAgreement"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_MasterServiceAgreement"
---

# [REST Example](#getFile-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFile-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_MasterServiceAgreement/getFile'
```
