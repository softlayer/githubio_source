---
title: "isConnectedToPrivateEndpointService"
description: "Accessing select IBM Cloud services attached to the private back-end network is made possible by establishing a network relationship between an account's private network and the Service Endpoint network. 



<h2>Responses</h2> 

<code>True</code> The account and Service Endpoint networks are currently connected. 

<code>False</code> The account and Service Endpoint networks are not connected; both networks are properly configured to connect. 



<h2>Exceptions</h2> 

<code>SoftLayer_Exception_NotReady</code> Thrown when the current network configuration will not support connection alteration. 



"
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network/isConnectedToPrivateEndpointService'
```
