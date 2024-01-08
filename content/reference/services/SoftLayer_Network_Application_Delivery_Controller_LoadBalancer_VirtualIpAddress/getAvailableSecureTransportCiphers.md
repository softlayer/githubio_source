---
title: "getAvailableSecureTransportCiphers"
description: "Yields a list of the SSL/TLS encryption ciphers that are currently supported on this virtual IP address instance. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
---

### [REST Example](#getAvailableSecureTransportCiphers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAvailableSecureTransportCiphers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressID}/getAvailableSecureTransportCiphers'
```
