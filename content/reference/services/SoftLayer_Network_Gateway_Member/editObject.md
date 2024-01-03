---
title: "editObject"
description: "Edit this member, only manufacturer and version can be changed "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Member"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway_Member"
---

# [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Gateway_Member]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway_Member/{SoftLayer_Network_Gateway_MemberID}/editObject'
```
