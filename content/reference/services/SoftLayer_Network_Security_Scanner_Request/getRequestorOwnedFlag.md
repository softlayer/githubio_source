---
title: "getRequestorOwnedFlag"
description: "Flag whether the requestor owns the hardware the scan was run on. This flag will return for hardware servers only, virtual servers will result in a null return even if you have a request out for them."
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

### [REST Example](#getRequestorOwnedFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRequestorOwnedFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Security_Scanner_Request/{SoftLayer_Network_Security_Scanner_RequestID}/getRequestorOwnedFlag'
```
