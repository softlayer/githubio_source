---
title: "disconnectPrivateEndpointService"
description: "Initiate the automated process to revoke mutual connectivity from the account network and IBM Cloud Service Endpoint network. Once initiated, the configuration process occurs asynchronously in the background. 



<h2>Responses</h2> 

<code>True</code> The request to disconnect was successfully initiated. 

<code>False</code> The account and Service Endpoint networks are already disconnected. 



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

### [REST Example](#disconnectPrivateEndpointService-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#disconnectPrivateEndpointService-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network/disconnectPrivateEndpointService'
```
