---
title: "getNetworkComponentFirewallProtectableIpAddresses"
description: "Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network component firewall. Note, this may not return all values for IPv6 subnets for this CloudLayer computing instance. Please use getFirewallProtectableSubnets to get all protectable subnets. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getNetworkComponentFirewallProtectableIpAddresses'
```
