---
title: "Get Dedicated Host Guests"
description: "Get a list of VSIs that have been deployed to a Dedicated Host. "
date: "2017-08-09"
classes:
    - "SoftLayer_Virtual_DedicatedHost"
tags:
---

```ruby
=begin
@author Ryan Tiffany
=end

require 'softlayer_api' 
require 'pp' 

# Connect to SoftLayer
client = SoftLayer::Client.new(:timeout => 120)

dedicated_host_id = 10501

getGuests = client['SoftLayer_Virtual_DedicatedHost'].object_with_id(dedicated_host_id).getGuests
pp getGuests
```