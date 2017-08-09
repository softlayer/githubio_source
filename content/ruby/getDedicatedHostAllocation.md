---
title: "Get Dedicated Host Allocation"
description: "Retrieve the CPU, Ram, Storage allocations on a dedicated host. "
date: "2017-08-09"
classes:
    - "SoftLayer_Virtual_DedicatedHost"
tags:
	- "getAllocationStatus"
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

getAllocStats = client['SoftLayer_Virtual_DedicatedHost'].object_with_id(dedicated_host_id).getAllocationStatus

pp getAllocStats
```