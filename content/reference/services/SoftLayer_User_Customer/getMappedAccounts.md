---
title: "getMappedAccounts"
description: "An OpenIdConnect identity, for example an IBMid, can be linked or mapped to one or more individual SoftLayer users, but no more than one SoftLayer user per account. This effectively links the OpenIdConnect identity to those accounts. This API returns a list of all the accounts for which there is a link between the OpenIdConnect identity and a SoftLayer user. Invoke this only on IBMid-authenticated users. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

# [REST Example](#getMappedAccounts-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getMappedAccounts-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/getMappedAccounts'
```
