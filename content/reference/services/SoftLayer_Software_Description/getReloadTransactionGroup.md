---
title: "getReloadTransactionGroup"
description: "The transaction group that a software description belongs to. A transaction group is a sequence of transactions that must be performed in a specific order for the installation of software."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Description"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Description"
---

### [REST Example](#getReloadTransactionGroup-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getReloadTransactionGroup-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Description/{SoftLayer_Software_DescriptionID}/getReloadTransactionGroup'
```
