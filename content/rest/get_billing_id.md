---
title: "Find a billing item from a provisioned product"
description: "Determine the billing item of a provisioned product using getBillingItem"

date: "2015-12-30"
classes: ["SoftLayer_Network_Storage"]
tags:
  - "billing"
  - "getBillingItem"
---

Operation: `GET`

Method: [`SoftLayer_Network_Storage::getBillingItem()`](http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/getBillingItem)

URL: SoftLayer_Network_Storage/getBillingItem

To find a billing item of a provisioned product you would use the `getBillingItem` call on the specific resource you are trying to locate. In the following example we are looking for the Billing Item of an Endurance Storage volume with an ID of 1234567.

Example CURL:
```
curl -su userid:api_key https://api.softlayer.com/rest/v3/SoftLayer_Network_Storage/1234567/getBillingItem
```

Example Response:
```json
{
    "allowCancellationFlag": 1,
    "cancellationDate": null,
    "categoryCode": "storage_service_enterprise",
    "createDate": "2015-11-17T12:14:14-06:00",
    "cycleStartDate": "2015-12-04T00:07:24-06:00",
    "description": "Endurance Storage",
    "id": "87654321",
    "laborFee": "0",
    "laborFeeTaxRate": "0",
    "lastBillDate": "2015-12-04T00:07:24-06:00",
    "modifyDate": "2015-12-04T00:07:24-06:00",
    "nextBillDate": "2016-01-04T00:00:00-06:00",
    "oneTimeFee": "0",
    "oneTimeFeeTaxRate": "0",
    "orderItemId": 99999999,
    "parentId": null,
    "recurringFee": "0",
    "recurringFeeTaxRate": "0",
    "recurringMonths": 1,
    "serviceProviderId": 1,
    "setupFee": "0",
    "setupFeeTaxRate": "0"
}
```
