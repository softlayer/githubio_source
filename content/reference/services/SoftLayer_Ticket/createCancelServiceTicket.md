---
title: "createCancelServiceTicket"
description: "A cancel service request creates a sales ticket. The hardware ID parameter is required to determine which server is to be cancelled. 

The reason parameter could be from the list below: 
* 'No longer needed'
* 'Business closing down'
* 'Server / Upgrade Costs'
* 'Migrating to larger server'
* 'Migrating to smaller server'
* 'Migrating to a different SoftLayer datacenter'
* 'Network performance / latency'
* 'Support response / timing'
* 'Sales process / upgrades'
* 'Moving to competitor'


The content parameter describes further the reason for cancelling service. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string, string, enum]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/createCancelServiceTicket'
```
