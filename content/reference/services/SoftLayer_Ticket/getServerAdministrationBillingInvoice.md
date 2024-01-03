---
title: "getServerAdministrationBillingInvoice"
description: "The invoice associated with a ticket. Only tickets with an associated administrative charge have an invoice."
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

# [REST Example](#getServerAdministrationBillingInvoice-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServerAdministrationBillingInvoice-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getServerAdministrationBillingInvoice'
```
