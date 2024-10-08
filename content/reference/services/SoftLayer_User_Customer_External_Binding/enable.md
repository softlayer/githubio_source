---
title: "enable"
description: "Enabling an external binding will activate the binding on your account and require you to authenticate with our trusted 3rd party 2 form factor vendor when logging into the SoftLayer customer portal. 

Please note that API access will be disabled for users that have an active external binding. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_External_Binding"
---

### [REST Example](#enable-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#enable-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_External_Binding/{SoftLayer_User_Customer_External_BindingID}/enable'
```
