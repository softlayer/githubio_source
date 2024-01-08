---
title: "createUpgradeTicket"
description: "Create a ticket for the SoftLayer sales team to perform a hardware or service upgrade. Our sales team will work with you on upgrade feasibility and pricing and then send the upgrade ticket to the proper department to perform the actual upgrade. Service affecting upgrades, such as server hardware or CloudLayer Computing Instance upgrades that require the server powered down must have a two hour maintenance specified for our datacenter engineers to perform your upgrade. Account level upgrades, such as adding PPTP VPN users, CDNLayer accounts, and monitoring services are processed much faster and do not require a maintenance window. "
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

### [REST Example](#createUpgradeTicket-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createUpgradeTicket-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, string, string, string, enum, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/createUpgradeTicket'
```
