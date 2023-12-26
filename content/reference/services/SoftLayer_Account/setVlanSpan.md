---
title: "setVlanSpan"
description: "Set the flag that enables or disables automatic private network VLAN spanning for a SoftLayer customer account. Enabling VLAN spanning allows an account's servers to talk on the same broadcast domain even if they reside within different private vlans. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/setVlanSpan'
```
