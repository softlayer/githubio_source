---
title: "setPrivateNetworkInterfaceSpeed"
description: "Sets the private network interface speed to the new speed. Speed values can only be 0 (Disconnect), 10, 100, or 1000. The new speed must be equal to or less than the max speed of the interface. 

It will take less than a minute to update the port speed. "
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

### [REST Example](#setPrivateNetworkInterfaceSpeed-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setPrivateNetworkInterfaceSpeed-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/setPrivateNetworkInterfaceSpeed'
```
