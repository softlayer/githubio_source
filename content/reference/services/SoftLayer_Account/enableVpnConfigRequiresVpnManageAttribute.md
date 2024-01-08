---
title: "enableVpnConfigRequiresVpnManageAttribute"
description: "Enables the VPN_CONFIG_REQUIRES_VPN_MANAGE attribute on the account. If the attribute does not exist for the account, it will be created and set to true. "
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

### [REST Example](#enableVpnConfigRequiresVpnManageAttribute-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#enableVpnConfigRequiresVpnManageAttribute-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/enableVpnConfigRequiresVpnManageAttribute'
```
