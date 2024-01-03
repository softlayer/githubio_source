---
title: "disable"
description: "Disabling an external binding will allow you to keep the external binding on your SoftLayer account, but will not require you to authentication with our trusted 2 form factor vendor when logging into the SoftLayer customer portal. 

You may supply one of the following reason when you disable an external binding: 
*Unspecified
*TemporarilyUnavailable
*Lost
*Stolen"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_External_Binding_Verisign"
---

# [REST Example](#disable-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#disable-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_External_Binding_Verisign/{SoftLayer_User_Customer_External_Binding_VerisignID}/disable'
```
