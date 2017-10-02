---
title: "Get Dedicated Host Guests"
description: "Get a list of VSIs that have been deployed to a Dedicated Host. "
date: "2017-08-09"
classes:
    - "SoftLayer_Virtual_DedicatedHost"
    - "SoftLayer_Account"
tags:
    - "getDedicatedHosts"
    - "getGuests"	
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


Once you have the Dedicated Host ID you can use the following code to retrieve the Virtual Guests on the host.

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
