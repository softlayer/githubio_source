---
title: "getReferralPartner"
description: "The Referral Partner who referred this order. (Only necessary for new customer orders)"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order"
---

### [REST Example](#getReferralPartner-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getReferralPartner-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/getReferralPartner'
```
