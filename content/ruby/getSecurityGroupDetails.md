---
title: "Get Security Group Details"
description: "Get the rules and associated servers in a Security Group."
date: "2017-08-09"
classes:
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "getAllObjects"
---

```ruby

=begin
@author Ryan Tiffany
=end

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)
secGroupId = 70501

getAll = client['SoftLayer_Network_SecurityGroup'].object_with_id(secGroupId).getAllObjects
pp getAll
```
