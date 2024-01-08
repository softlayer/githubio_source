---
title: "getValidSecurityCertificateEntries"
description: "Retrieve a list of valid (non-expired) security certificates without the sensitive certificate information. This allows non-privileged users to view and select security certificates when configuring associated services. "
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

### [REST Example](#getValidSecurityCertificateEntries-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getValidSecurityCertificateEntries-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getValidSecurityCertificateEntries'
```
