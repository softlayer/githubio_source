---
title: "Migrate a VSI between dedicated hosts"
description: "Migrate a Dedicated Host instance to another Dedicated Host. You can migrate your dedicated host instances from one host to another within the same POD."
date: "2017-08-04"
classes:
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "migrateDedicatedHost"
    - "getDedicatedHosts"
---

The first thing you need to get is a list of the Dedicated Hosts on your account. To list the Dedicated Hosts on your account you can use the following code:

```ruby

require 'softlayer_api' 
require 'pp' 

# Connect to SoftLayer
client = SoftLayer::Client.new(:timeout => 120)

getDediHosts = client['SoftLayer_Account'].getDedicatedHosts
pp getDediHosts
```

Once you have the Dedicated Host ID you can use the following code to migrate the Virtual Guest to another host. This script will kick of an immediate migration of the Virtual Guest.

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
