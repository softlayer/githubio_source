---
title: "getObject"
description: "getObject retrieves the SoftLayer_Ticket_Update_Employee object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Ticket_Update_Employee service. You can only retrieve employee updates to tickets that your API account has access to. "
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

### [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Ticket_Update_Employee/{SoftLayer_Ticket_Update_EmployeeID}/getObject'
```
