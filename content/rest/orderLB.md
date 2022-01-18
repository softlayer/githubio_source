---
title: "Order a Local Load Balancer"
description: "Use verifyOrder and placeOrder to order a new Local Load Balancer"

date: "2016-05-05"
classes: ["SoftLayer_Product_Order"]
tags:
  - "verifyorder"
  - "placeorder"
---

Operation: `POST`

Method: [`SoftLayer_Product_Order::verifyOrder()`](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder)
Method: [`SoftLayer_Product_Order::placeOrder()`](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder)

URL: SoftLayer_Product_Order/verifyOrder
URL: SoftLayer_Product_Order/placeOrder

In the following example I am ordering a Local Load Balancer 500 VIP connections (PriceId: 2078) in the Dallas 06 Datacenter (locationId: 154820).


Example CURL using verifyOrder: 
```
curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -k -X POST -d '{"parameters":[{"packageId":194,"location":154820,"quantity":1,"prices":[{"id":2078}]}]}' "https://api.softlayer.com/rest/v3/SoftLayer_Product_Order/verifyOrder"
```

Example CURL using placeOrder: 
```
curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -k -X POST -d '{"parameters":[{"packageId":194,"location":154820,"quantity":1,"prices":[{"id":2078}]}]}' "https://api.softlayer.com/rest/v3/SoftLayer_Product_Order/placeOrder"
```

