---
title: "Show storage on all Virtual Guests"
description: "Show all block devices connected to your Virtual Guests as well as type and capacity of each block device."
date: "2017-04-03"
classes: ["SoftLayer_Account"]
tags:
    - "objectMask"
    - "blockDevices"
---


```ruby
require 'softlayer_api'
require 'pp'

# Create a SoftLayer API client object
client = SoftLayer::Client.new()

account_service = client['SoftLayer_Account']

# We will retrieve the additional information for each VSI:
mask = 'mask[id,hostname,blockDevices[id,mountType,diskImage[capacity]]]'
begin
  # getVirtualGuests() will get all the VSIs that an account has.
  result = account_service.object_mask(mask).getVirtualGuests
  pp result
rescue StandardError => exception
  puts "Unable to  get the VSIs: #{exception}"
end
```