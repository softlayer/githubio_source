---
title: "createObject"
description: "Passing in an unsaved instances of a Query_Host object into this function will create the object and return the results to the user. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Monitor_Version1_Query_Host"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Monitor_Version1_Query_Host]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Monitor_Version1_Query_Host/createObject'
```
