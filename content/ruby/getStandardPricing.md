---
title: "Find standard location pricing for a package"
description: "Use an object filter to only return the Standard Location pricing for a SoftLayer package. This is a priceItemId that is standard accross all SoftLayer Datacenters"
date: "2016-09-01"
classes: ["SoftLayer_Product_Package"]
tags:
    - "object_filter"
    - "pricing"
---

```ruby 
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

object_filter = SoftLayer::ObjectFilter.new do |object_filter|
  object_filter.accept('items.prices.locationGroupId').when_it is_null
end

location = client['SoftLayer_Product_Package']
result = location.object_with_id(46).object_filter(object_filter).getItems

pp result
```
