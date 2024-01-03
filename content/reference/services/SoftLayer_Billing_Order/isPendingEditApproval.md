---
title: "isPendingEditApproval"
description: "When an order has been modified, it will contain a status indicating so. This method checks that status and also verifies that the active user's account is the same as the account on the order. "
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

# [REST Example](#isPendingEditApproval-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isPendingEditApproval-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order/{SoftLayer_Billing_OrderID}/isPendingEditApproval'
```
