---
title: "enableVrf"
description: "Initiate the change of the private network to VRF, which will cause a brief private network outage. 

@SLDNDocumentation Method Permissions NETWORK_VLAN_SPANNING 

<h2>Responses</h2> 

<code>True</code> The request to change the private network has been accepted and the change will begin immediately. 

<code>False</code> The request had no change because the private network is already in a VRF or in the process of converting to VRF. 

<h2>Exceptions</h2> 

<code>SoftLayer_Exception_NotReady</code> Thrown when the current private network cannot be converted to VRF without specialized assistance. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network"
---

### [REST Example](#enableVrf-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#enableVrf-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network/enableVrf'
```
