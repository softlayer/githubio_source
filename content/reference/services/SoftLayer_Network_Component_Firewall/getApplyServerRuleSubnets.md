---
title: "getApplyServerRuleSubnets"
description: "The additional subnets linked to this network component firewall, that inherit rules from the host that the context slot is attached to."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Firewall"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Component_Firewall"
---

### [REST Example](#getApplyServerRuleSubnets-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getApplyServerRuleSubnets-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component_Firewall/{SoftLayer_Network_Component_FirewallID}/getApplyServerRuleSubnets'
```
