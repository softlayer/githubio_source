---
title: "Find a billing item from a provisioned product"
description: "Determine the billing item of a provisioned product using getBillingItem"
date: "2016-01-29"
classes: ["SoftLayer_Network_Storage"]
tags:
    - "getbillingitem"
    - "objectmask"
---

In the following example we are looking for the Billing Item of an Endurance Storage volume with an ID of 1234567.

```ruby
# add your network storage id, it can be found by doing this call: http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNasNetworkStorage
network_storage_id = 1234567
#
item = client[:Network_Storage].object_mask("mask[billingItem[createDate,hoursUsed,hourlyRecurringFee,currentHourlyCharge]]").object_with_id(network_storage_id).getObject
pp item['billingItem']
```
