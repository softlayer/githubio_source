---
title: "getStatisticsGraph"
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

### [REST Example](#getStatisticsGraph-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getStatisticsGraph-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Message_Delivery_Email_Sendgrid/{SoftLayer_Network_Message_Delivery_Email_SendgridID}/getStatisticsGraph'
```
