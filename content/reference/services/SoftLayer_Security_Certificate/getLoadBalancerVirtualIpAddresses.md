---
title: "getLoadBalancerVirtualIpAddresses"
description: "The load balancers virtual IP addresses currently associated with the certificate."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate"
type: "reference"
layout: "method"
mainService : "SoftLayer_Security_Certificate"
---

# [REST Example](#getLoadBalancerVirtualIpAddresses-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getLoadBalancerVirtualIpAddresses-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Security_Certificate/{SoftLayer_Security_CertificateID}/getLoadBalancerVirtualIpAddresses'
```
