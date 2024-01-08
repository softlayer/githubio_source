---
title: "addResponseRating"
description: "As part of the customer service process SoftLayer has provided a quick feedback mechanism for its customers to rate the responses that its employees give on tickets. addResponseRating() sets the rating for a single ticket update made by a SoftLayer employee. Ticket ratings have the integer values 1 through 5, with 1 being the worst and 5 being the best. Once the rating is set ''addResponseRating()'' returns a boolean true. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Update_Employee"
type: "reference"
layout: "method"
mainService : "SoftLayer_Ticket_Update_Employee"
---

### [REST Example](#addResponseRating-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addResponseRating-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [int, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket_Update_Employee/{SoftLayer_Ticket_Update_EmployeeID}/addResponseRating'
```
