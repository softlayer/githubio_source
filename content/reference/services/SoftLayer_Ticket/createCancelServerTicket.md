---
title: "createCancelServerTicket"
description: "A cancel server request creates a ticket to cancel the resource on next bill date. The hardware ID parameter is required to determine which server is to be cancelled. NOTE: Hourly bare metal servers will be cancelled on next bill date. 

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


The content parameter describes further the reason for cancelling the server. "
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

# [REST Example](#createCancelServerTicket-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createCancelServerTicket-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string, string, boolean, enum]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/createCancelServerTicket'
```
