---
title: "updateFirewallIntraVlanCommunication"
description: "
*** DEPRECATED ***
Updates the firewall associated to this VLAN to allow or disallow intra-VLAN communication. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan"
---

### [REST Example](#updateFirewallIntraVlanCommunication-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateFirewallIntraVlanCommunication-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/updateFirewallIntraVlanCommunication'
```
