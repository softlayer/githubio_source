---
title: "getServiceBillingItemsByCategory"
description: "This service returns billing items of a specified category code. This service should be used to retrieve billing items that you wish to cancel. Some billing items can be canceled via [SoftLayer_Security_Certificate_Request](/reference/datatypes/SoftLayer_Security_Certificate_Request) service. 

In order to find billing items for cancellation, use [SoftLayer_Product_Item_Category::getValidCancelableServiceItemCategories](/reference/datatypes/$1/#$2) service to retrieve category codes that are eligible for cancellation. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---

### [REST Example](#getServiceBillingItemsByCategory-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getServiceBillingItemsByCategory-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Virtual_DedicatedHost/getServiceBillingItemsByCategory'
```
