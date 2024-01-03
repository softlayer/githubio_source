---
title: "getSmtpAccess"
description: "A flag that determines if a SendGrid e-mail delivery account has access to send mail through the SendGrid SMTP server."
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

# [REST Example](#getSmtpAccess-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSmtpAccess-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Message_Delivery_Email_Sendgrid/{SoftLayer_Network_Message_Delivery_Email_SendgridID}/getSmtpAccess'
```
