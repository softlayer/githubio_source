---
title: "getReport"
description: "Get the vulnerability report for a scan request, formatted as HTML string. Previous scan reports are held indefinitely. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Security_Scanner_Request"
---

# [REST Example](#getReport-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getReport-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Security_Scanner_Request/{SoftLayer_Network_Security_Scanner_RequestID}/getReport'
```
