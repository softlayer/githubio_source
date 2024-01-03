---
title: "createAdministrativeTicket"
description: "Create an administrative support ticket. Use an administrative ticket if you require SoftLayer's assistance managing your server or content. If you are experiencing an issue with SoftLayer's hardware, network, or services then please open a standard support ticket. 

Support tickets may only be created in the open state. The SoftLayer API defaults new ticket properties ''userEditableFlag'' to true, ''accountId'' to the id of the account that your API user belongs to, and ''statusId'' to 1001 (or 'open'). You may not assign your new to ticket to users that your API user does not have access to. 

Once your ticket is created it is placed in a queue for SoftLayer employees to work. As they update the ticket new [SoftLayer_Ticket_Update](/reference/datatypes/SoftLayer_Ticket_Update) entries are added to the ticket object. 

Administrative support tickets add a one-time $3USD charge to your account. "
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

# [REST Example](#createAdministrativeTicket-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createAdministrativeTicket-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Ticket, string, int, string, string, string, SoftLayer_Container_Utility_File_Attachment, enum]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket/createAdministrativeTicket'
```
