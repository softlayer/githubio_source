---
title: "Determining your next bill"
description: "Example on how to use getNextInvoiceTotalAmount to retrieve the pre-tax total amount of an account's next invoice measured in US Dollars ($USD). The amount assumes no changes or charges occur between now and the time of billing.

"
date: "2015-12-30"
classes: ["SoftLayer_Account"]
tags:
  - "billing"
  - "getNextInvoiceTotalAmount"
---

Operation: `GET`

Method: [`SoftLayer_Account::getNextInvoiceTotalAmount()`](http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNextInvoiceTotalAmount)

URL: SoftLayer_Account/getNextInvoiceTotalAmount

Example CURL:
```
curl -su userid:api_key https://api.softlayer.com/rest/v3/SoftLayer_Account/getNextInvoiceTotalAmount
```

Example Response:
```
250.26
```
