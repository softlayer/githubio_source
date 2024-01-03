---
title: "inviteUserToLinkOpenIdConnect"
description: "Send email invitation to a user to join a SoftLayer account and authenticate with OpenIdConnect. Throws an exception on error. "
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

# [REST Example](#inviteUserToLinkOpenIdConnect-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#inviteUserToLinkOpenIdConnect-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/inviteUserToLinkOpenIdConnect'
```
