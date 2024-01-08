---
title: "disable"
description: "Completely restrict all incoming and outgoing bandwidth traffic to a network component "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Network_Component"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest_Network_Component"
---

### [REST Example](#disable-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#disable-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest_Network_Component/{SoftLayer_Virtual_Guest_Network_ComponentID}/disable'
```
