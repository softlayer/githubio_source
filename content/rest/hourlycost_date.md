---
title: "Month-to-date cost of a Virtual_Guest"
description: "Determine the month-to-date cost of an hourly Virtual_Guest using getBillingItem and an objectMask"

date: "2015-12-30"
classes: ["SoftLayer_Virtual_Guest"]
tags:
  - "getBillingItem"
  - "billing"
  - "objectMask"
---

Operation: `GET`

Method: [`SoftLayer_Virtual_Guest::getBillingItem()`](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getBillingItem)

URL: SoftLayer_Virtual_Guest/<virtual_guest_id>/getBillingItem?objectMask=mask[createDate,hoursUsed,hourlyRecurringFee,currentHourlyCharge]

Example CURL:
```
curl -su userid:api_key https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/<virtual_guest_id>/getBillingItem?objectMask=mask[createDate,hoursUsed,hourlyRecurringFee,currentHourlyCharge]
```

Example Response:
```json
{
    "createDate": "2015-12-30T09:26:32-06:00",
    "currentHourlyCharge": ".18",
    "hourlyRecurringFee": ".09",
    "hoursUsed": "2"
}
```
