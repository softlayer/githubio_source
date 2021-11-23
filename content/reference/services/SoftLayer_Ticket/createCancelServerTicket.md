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
    - "createCancelServerTicket"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket"
---
