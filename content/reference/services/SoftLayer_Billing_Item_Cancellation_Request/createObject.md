---
title: "createObject"
description: "This method creates a service cancellation request. 

You need to have 'Cancel Services' privilege to create a cancellation request. You have to provide at least one SoftLayer_Billing_Item_Cancellation_Request_Item in the 'items' property. Make sure billing item's category code belongs to the cancelable product codes. You can retrieve the cancelable product category by the [SoftLayer_Product_Item_Category::getValidCancelableServiceItemCategories](/reference/datatypes/$1/#$2) service. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
type: "reference"
layout: "method"
mainService : "SoftLayer_Billing_Item_Cancellation_Request"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Billing_Item_Cancellation_Request]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Item_Cancellation_Request/createObject'
```
