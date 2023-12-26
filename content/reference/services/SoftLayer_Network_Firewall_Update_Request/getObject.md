---
title: "getObject"
description: "''getObject'' returns a SoftLayer_Network_Firewall_Update_Request object. You can only get historical objects for servers attached to your account that have a network firewall enabled. ''createObject'' inserts a new SoftLayer_Network_Firewall_Update_Request object. You can only insert requests for servers attached to your account that have a network firewall enabled. ''getFirewallUpdateRequestRuleAttributes'' Get the possible attribute values for a firewall update request rule. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Firewall_Update_Request/{SoftLayer_Network_Firewall_Update_RequestID}/getObject'
```
