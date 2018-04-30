---
title: "RestFulCreateServer.txt"
description: "RestFulCreateServer.txt"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
URL: https://$USERNAME:$APIKEY@api.softlayer.com/rest/v3/SoftLayer_Product_Order/placeOrder.json
Method: POST
JSON: {
    "parameters": [
        {
            "quantity": 1,
            "location": "AMSTERDAM",
            "packageId": 145,
            "prices": [
                {
                    "id": 17231
                },
                {
                    "id": 637
                },
                {
                    "id": 682
                },
                {
                    "id": 876
                },
                {
                    "id": 19087
                },
                {
                    "id": 342
                },
                {
                    "id": 273
                },
                {
                    "id": 55
                },
                {
                    "id": 58
                },
                {
                    "id": 420
                },
                {
                    "id": 418
                },
                {
                    "id": 21
                },
                {
                    "id": 57
                },
                {
                    "id": 906
                }
            ],
            "hardware": [
                {
                    "hostname": "test",
                    "domain": "example.org"
                }
            ]
        }
    ]
}
```
