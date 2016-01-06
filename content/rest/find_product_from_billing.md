---
title: "Find provisioned product from a billing item"
description: "Associate a billing item ID with a SoftLayer service or product using getAssociatedParent"

date: "2015-12-30"
classes: ["SoftLayer_Billing_Item"]
tags:
  - "billing"
  - "getAssociatedParent"
---

Operation: `GET`

Method: [`SoftLayer_Billing_Item::getAssociatedParent()`](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/getAssociatedParent)

URL: SoftLayer_Billing_Item/getAssociatedParent

Example CURL:
```
curl -su userid:api_key https://api.softlayer.com/rest/v3/SoftLayer_Billing_Item/<billing_item_id>/getAssociatedParent?objectMask=mask\[categoryCode,id,description\]
```

Example Response:
```json
[
    {
        "categoryCode": "storage_service_enterprise",
        "description": "Endurance Storage",
        "id": 1234321
    }
]
```
