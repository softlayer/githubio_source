---
title: "getLastKnownPowerState"
description: "The last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#getLastKnownPowerState-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLastKnownPowerState-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getLastKnownPowerState'
```
