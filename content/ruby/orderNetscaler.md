---
title: "Order a Netscaler"
description: "Example of how to order a NetScaler ADC."
date: "2017-03-31"
classes:
    - "SoftLayer_Product_Order"
tags:
    - "netscaler"
    - "vpx"
    - "load balancer"
---

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

config = { 
    'orderContainers' => [
        {"hardware" => [{
            "primaryBackendNetworkComponent" => {
                    # REPLACE THIS
                    "networkVlanId" => 1211234
                },
                "primaryNetworkComponent" => {
                    # REPLACE THIS
                    "networkVlanId" => 1212456
                }
            }],
            # REPLACE THIS with your location
            "location" => "DALLAS09",
            "packageId" => 192,
            "quantity" => 1,
            # Price IDS for Netscaler and 2 IPs
            "prices" => [
                {"id" => 44964},
                {"id" => 17238}
            ]
            }]
        }

order = client['Product_Order'].verifyOrder(config)

pp order    
```
