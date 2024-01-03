---
title: "getAuthorizingUser"
description: "The user that authorized this firewall update request."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Firewall_Update_Request"
---

# [REST Example](#getAuthorizingUser-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAuthorizingUser-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Firewall_Update_Request/{SoftLayer_Network_Firewall_Update_RequestID}/getAuthorizingUser'
```
