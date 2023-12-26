---
title: "disableVpnConfigRequiresVpnManageAttribute"
description: "Disables the VPN_CONFIG_REQUIRES_VPN_MANAGE attribute on the account. If the attribute does not exist for the account, it will be created and set to false. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/disableVpnConfigRequiresVpnManageAttribute'
```
