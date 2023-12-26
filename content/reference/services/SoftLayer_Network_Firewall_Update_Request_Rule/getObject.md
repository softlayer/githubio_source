---
title: "getObject"
description: "getObject returns a SoftLayer_Network_Firewall_Update_Request_Rule object. You can only get historical objects for servers attached to your account that have a network firewall enabled. createObject inserts a new SoftLayer_Network_Firewall_Update_Request_Rule object. Use the SoftLayer_Network_Firewall_Update_Request to create groups of rules for an update request. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Firewall_Update_Request_Rule"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Firewall_Update_Request_Rule/{SoftLayer_Network_Firewall_Update_Request_RuleID}/getObject'
```
