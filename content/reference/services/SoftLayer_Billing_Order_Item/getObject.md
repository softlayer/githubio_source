---
title: "getObject"
description: "getObject retrieves the SoftLayer_Billing_Item object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Billing_Item service. You can only retrieve billing items tied to the account that your portal user is assigned to. Billing items are an account's items of billable items. There are 'parent' billing items and 'child' billing items. The server billing item is generally referred to as a parent billing item. The items tied to a server, such as ram, harddrives, and operating systems are considered 'child' billing items. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Item"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Order_Item"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Item/{SoftLayer_Billing_Order_ItemID}/getObject'
```
