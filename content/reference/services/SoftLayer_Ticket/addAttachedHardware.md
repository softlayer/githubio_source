---
title: "addAttachedHardware"
description: "Attach the given hardware to a SoftLayer ticket. A hardware attachment provides an easy way for SoftLayer's employees to quickly look up your hardware records in the case of hardware-specific issues. "
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

# [REST Example](#addAttachedHardware-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addAttachedHardware-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/addAttachedHardware'
```
