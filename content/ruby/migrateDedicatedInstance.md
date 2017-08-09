---
title: "Migrate a VSI between dedicated hosts"
description: "Migrate a Dedicated Host instance to another Dedicated Host. You can migrate your dedicated host instances from one host to another within the same POD."
date: "2017-08-04"
classes:
    - "SoftLayer_Virtual_Guest"
tags:
---

This script will kick of an immediate migration of the Virtual Guest.

```ruby 

=begin
@author Ryan Tiffany
=end

require 'softlayer_api' 
require 'pp' 

# Connect to SoftLayer
client = SoftLayer::Client.new(:timeout => 120)

destinationHostId = 10001
vsiId = 37167483

migrateGuest = client['SoftLayer_Virtual_Guest'].object_with_id(vsiId).migrateDedicatedHost(destinationHostId)
pp migrateGuest
```