---
title: "editObject"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Message_Delivery_Email_Sendgrid"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Message_Delivery_Email_Sendgrid"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Message_Delivery]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Message_Delivery_Email_Sendgrid/{SoftLayer_Network_Message_Delivery_Email_SendgridID}/editObject'
```
