---
title: "receiveEventDirect"
description: "Modifies linked Paas user data based on changes initiated by Bluemix."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Profile_Event_HyperWarp"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_Profile_Event_HyperWarp"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_User_Customer_Profile_Event_HyperWarp_ProfileChange]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_Profile_Event_HyperWarp/receiveEventDirect'
```
