---
title: "getInvoiceItems"
description: "The invoice items associated with a ticket. Ticket based invoice items only exist when a ticket incurs a fee that has been invoiced."
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

### [REST Example](#getInvoiceItems-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getInvoiceItems-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/{SoftLayer_TicketID}/getInvoiceItems'
```
