---
title: "getCoreRestrictedOperatingSystemPrice"
description: "If the virtual server currently has an operating system that has a core capacity restriction, return the associated core-restricted operating system item price. Some operating systems (e.g., Red Hat Enterprise Linux) may be billed by the number of processor cores, so therefore require that a certain number of cores be present on the server. "
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

### [REST Example](#getCoreRestrictedOperatingSystemPrice-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getCoreRestrictedOperatingSystemPrice-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getCoreRestrictedOperatingSystemPrice'
```
