---
title: "getSecurityCertificateEntry"
description: "The SSL certificate currently associated with the VIP. Provides chosen certificate visibility to unprivileged users."
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

### [REST Example](#getSecurityCertificateEntry-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSecurityCertificateEntry-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressID}/getSecurityCertificateEntry'
```
