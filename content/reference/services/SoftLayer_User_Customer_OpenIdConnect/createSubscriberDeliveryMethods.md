---
title: "createSubscriberDeliveryMethods"
description: "Create delivery methods for a notification that the user is subscribed to. Multiple delivery method keyNames can be supplied to create multiple delivery methods for the specified notification. Available delivery methods - 'EMAIL'. Available notifications - 'PLANNED_MAINTENANCE', 'UNPLANNED_INCIDENT'. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

# [REST Example](#createSubscriberDeliveryMethods-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createSubscriberDeliveryMethods-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/createSubscriberDeliveryMethods'
```
