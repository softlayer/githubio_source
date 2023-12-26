---
title: "restoreDefaults"
description: "This will completely reset the firewall to factory settings. If the firewall is not a FSA 10G appliance an error will occur. Note, this process is performed asynchronously. During the process all traffic will not be routed through the firewall. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan_Firewall"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan_Firewall/{SoftLayer_Network_Vlan_FirewallID}/restoreDefaults'
```
