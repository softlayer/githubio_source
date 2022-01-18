---
title: "Create a new Bandwidth Pool"
description: "This allows you to optimize your bandwidth usage by _pooling_ all of the bandwidth together for servers in a the Pool."
date: "2016-08-15"
classes: ["SoftLayer_Network_Bandwidth_Version1_Allotment"]
tags:
    - "ordertemplate"
    - "createobject"
---

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new(:timeout => 120)
object_id = nil

orderTemplate = {
   'accountId' => xxxxx,
   'bandwidthAllotmentTypeId' => 2,
   'locationGroupId' => 1,
   'name' => 'newRubyBwPool'
}

orderPool = client['SoftLayer_Network_Bandwidth_Version1_Allotment']
item = orderPool.object_with_id(object_id).createObject(orderTemplate)

pp item
```
