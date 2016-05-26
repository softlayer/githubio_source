---
title: "Find out which user placed an order"
description: "Find out which user placed an orde"

date: "2016-05-26"
classes:
  - "SoftLayer_Account"
  - "SoftLayer_Billing_Order"
tags:
  - "billing"
  - "users"
---

Operation: `GET`

Method: [`SoftLayer_Account::getOrders()`](http://sldn.softlayer.com/reference/services/SoftLayer_Account/getOrders)

URL: SoftLayer_Account/getOrders

Example CURL:
```
curl -su userid:api_key "https://api.softlayer.com/rest/v3/SoftLayer_Account/getOrders?objectMask=mask\[userRecord\[username\]\]"
```

Example Response:
```
{
        "accountId": 1234,
        "createDate": "2014-02-04T11:45:47-06:00",
        "id": 99999999,
        "impersonatingUserRecordId": null,
        "modifyDate": "2014-02-04T11:45:53-06:00",
        "orderQuoteId": null,
        "orderTypeId": 7,
        "presaleEventId": null,
        "privateCloudOrderFlag": false,
        "status": "APPROVED",
        "userRecord": {
            "username": "SL1234"
        },
        "userRecordId": 111111
```


-------

Operation: `GET`

Method: [`SoftLayer_Billing_Order::getObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order/getObject)

URL: SoftLayer_Billing_Order/getObject

Example CURL:
```
curl -su userid:api_key "https://api.softlayer.com/rest/v3/SoftLayer_Billing_Order/99999999/getObject?objectMask=mask\[userRecord\[username\]\]"
```

Example Response:
```
{
        "accountId": 1234,
        "createDate": "2014-02-04T11:45:47-06:00",
        "id": 99999999,
        "impersonatingUserRecordId": null,
        "modifyDate": "2014-02-04T11:45:53-06:00",
        "orderQuoteId": null,
        "orderTypeId": 7,
        "presaleEventId": null,
        "privateCloudOrderFlag": false,
        "status": "APPROVED",
        "userRecord": {
            "username": "SL1234"
        },
        "userRecordId": 111111
```


### Note
specifying "userRecord[username]" in the objectMask will make the API call ONLY get the username for each order. The userRecord relational property pulls in quite a bit of additional data, so this lets the API skip getting that additional data, and can help speed up the API call. If additional properties are needed, they can be selected from the [SoftLayer_User_Customer](http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer) datatype.


Getting all of the users for all of the orders on accounts with many orders may take a while. If you know the order ID using the above REST call might be helpful