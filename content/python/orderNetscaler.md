---
title: "Order a Netscaler"
description: "Example of how to create a Domain in the SoftLayer DNS, along with how to edit its resource records."
date: "2016-11-29"
classes: 
    - "SoftLayer_Product_Order"
tags:
    - "netscaler"
    - "vpx"
    - "load balancer"
---
```
import SoftLayer
from pprint import pprint as pp

class orderNetscaler():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self):

        productOrder = {
        'orderContainers': [
            {"hardware": [{
                "primaryBackendNetworkComponent": {
                    # REPLACE THIS
                    "networkVlanId": 1234
                },
                "primaryNetworkComponent": {
                    # REPLACE THIS
                    "networkVlanId": 456
                }
            }],
            # REPLACE THIS with your location
            "location": "DALLAS09",
            "packageId": 192,
            "quantity": 1,
            # Price IDS for Netscaler and 2 IPs
            "prices": [
                {"id": 44964}, 
                {"id": 17238}
            ]
        }]
        }
        order = self.client['Product_Order'].placeOrder(productOrder)
        pp(order)

if __name__ == "__main__":
    main = example()
    main.main()
```