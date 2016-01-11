---
title: "Place quote order"
description: "Retrieve an order object from a quote and place an order based on it"
date: "2015-11-28"
classes: ["SoftLayer_Billing_Order_Quote"]
tags:
    - "order"
    - "quote"
---


```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the SoftLayer API are grabbed from the config file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new

QUOTE_ID = 1234

quote = client['Billing_Order_Quote'].object_with_id(QUOTE_ID)
puts "Displaying quote:\n"
pp quote.getRecalculatedOrderContainer['orderContainers'][0]

puts "Displaying order result:\n"
pp quote.placeOrder(
  complexType: 'Container_Product_Order_Virtual_Guest',
  hardware: [{ hostname: 'quotetest', domain: 'example.com' }],
  quantity: 1
)
```
