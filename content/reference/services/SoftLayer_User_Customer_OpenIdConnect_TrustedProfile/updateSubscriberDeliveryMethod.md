---
title: "updateSubscriberDeliveryMethod"
description: "Update a delivery method for a notification that the user is subscribed to. A delivery method keyName along with an active flag can be supplied to update the active status of the delivery methods for the specified notification. Available delivery methods - 'EMAIL'. Available notifications - 'PLANNED_MAINTENANCE', 'UNPLANNED_INCIDENT'. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
---

### [REST Example](#updateSubscriberDeliveryMethod-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateSubscriberDeliveryMethod-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile/{SoftLayer_User_Customer_OpenIdConnect_TrustedProfileID}/updateSubscriberDeliveryMethod'
```
