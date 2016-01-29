---
title: "Calculating month-to-date cost of a Virtual_Guest"
description: "Determine the month-to-date cost of an hourly Virtual_Guest using getBillingItem and an objectMask"
date: "2016-01-29"
classes: ["Virtual_Guest"]
tags:
    - "billing"
    - "objectMask"
---

```ruby
require 'softlayer_api' # Requires softlayer_api >= 3.2
require 'pp' # used to display results

# Create a client
client = SoftLayer::Client.new

# add your server id, can be found with the following script: https://softlayer.github.io/ruby/list_instances/
virtual_server_id = 12345678
item = client[:Virtual_Guest].object_mask("mask[billingItem[createDate,hoursUsed,hourlyRecurringFee,currentHourlyCharge]]").object_with_id(virtual_server_id).getObject
puts "Billing Item for Virtual Server:"
pp item['billingItem']
```

## Example Output

```
Billing Item for Virtual Server:
{"createDate"=>"2016-01-29T12:23:43-06:00",
 "currentHourlyCharge"=>".023",
 "hourlyRecurringFee"=>".023",
 "hoursUsed"=>"1"}
```
