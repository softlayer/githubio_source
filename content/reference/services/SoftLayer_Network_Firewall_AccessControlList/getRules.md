---
title: "getRules"
description: "The currently running rule set of this context access control list firewall."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_AccessControlList"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Firewall_AccessControlList"
---

### [REST Example](#getRules-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRules-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Firewall_AccessControlList/{SoftLayer_Network_Firewall_AccessControlListID}/getRules'
```
