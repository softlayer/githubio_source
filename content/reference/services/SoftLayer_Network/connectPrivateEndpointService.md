---
title: "connectPrivateEndpointService"
description: "Initiate the automated process to establish connectivity granting the account private back-end network access to the services available through IBM Cloud Service Endpoint. Once initiated, the configuration process occurs asynchronously in the background. 



<h2>Responses</h2> 

<code>True</code> The request to connect was successfully initiated. 

<code>False</code> The account and Service Endpoint networks are already connected. 



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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network/connectPrivateEndpointService'
```
