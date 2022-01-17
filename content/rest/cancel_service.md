---
title: "Cancel an item or service"
description: "Use cancelService to cancel an item or service"

date: "2015-12-30"
classes: ["SoftLayer_Billing_Item"]
tags:
  - "billing"
  - "cancelservice"
---

Operation: `GET`

Method: [`SoftLayer_Billing_Item::cancelService()`](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService)

URL: SoftLayer_Billing_Item/cancelService

Example CURL:
```
curl -su userid:api_key https://api.softlayer.com/rest/v3/SoftLayer_Billing_Item/<billing_item_id/cancelService
```

Example Response:
```
true
```

### Note
If you are wanting to use the REST API to cancel a Bare Metal server you cannot use the [cancelService](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService) call but rather you will need to utilize the [cancelItem](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem) call. This call and provide a cancellation reason.
