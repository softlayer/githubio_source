---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Monitor_Version1_Query_Host object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Monitor_Version1_Query_Host service. You can only retrieve query hosts attached to hardware that belong to your account. "
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

### [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Monitor_Version1_Query_Host/{SoftLayer_Network_Monitor_Version1_Query_HostID}/getObject'
```
