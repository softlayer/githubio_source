
---
title: "Find Location specific pricing for a package"
description: "Use an object filter to return the Location Based pricing information for a SoftLayer package."
date: "2016-09-01"
classes: ["SoftLayer_Product_Package"]
tags:
    - "objectfilter"
    - "objectmask"
    - "pricing"
---

With the introduction to Location-based Pricing, we updated our pricing model to represent the costs in each data center more clearly. Instead of adding premiums to a base server price, we have priced servers and services in each data center with their own location-based [SoftLayer_Product_Item_Price](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Item_Price) objects via the API. In the following example we will query for the Dallas 10 data center for SoftLayer Virtual Guests. 

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

object_filter = SoftLayer::ObjectFilter.new
object_filter.set_criteria_for_key_path('items.prices.locationGroupId',
	'operation' => 'in',
        'options' => [{
        'name' => 'data',
        'value' => 1441195
        }])


location = client['SoftLayer_Product_Package']
result = location.object_with_id(46).object_filter(object_filter).getItems

pp result
```
