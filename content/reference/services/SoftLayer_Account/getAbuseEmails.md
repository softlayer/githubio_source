---
title: "getAbuseEmails"
description: "Email addresses that are responsible for abuse and legal inquiries on behalf of an account. For instance, new legal and abuse tickets are sent to these addresses."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

# [REST Example](#getAbuseEmails-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAbuseEmails-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/{SoftLayer_AccountID}/getAbuseEmails'
```
