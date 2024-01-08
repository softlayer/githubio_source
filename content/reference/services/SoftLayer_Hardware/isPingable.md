---
title: "isPingable"
description: "The '''isPingable''' method issues a ping command to the selected server and returns the result of the ping command. This boolean return value displays ''true'' upon successful ping or ''false'' for a failed ping. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware"
---

### [REST Example](#isPingable-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isPingable-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware/{SoftLayer_HardwareID}/isPingable'
```
