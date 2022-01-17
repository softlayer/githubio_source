---
title: "Adding/Removing Servers in a Bandwidth Pool"
description: "Adding and removing Virtual Guests and Bare Metal Servers in an exising Bandwidth Pool"
date: "2016-08-22"
classes: ["SoftLayer_Network_Bandwidth_Version1_Allotment"]
tags:
    - "bandwidthpool"
---

The following script allows you to add and remove servers in an existing bandwidth pool. The script requires empty arrays when not specifying a Bare Metal or Virtual Guest Id.

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new(:timeout => 120)
pool_id = 123456

hardwareToAdd = []
hardwareToRemove = []
cloudsToAdd = [ {'id' => 23123143 } ]
cloudsToRemove = []

addRemove = client['SoftLayer_Network_Bandwidth_Version1_Allotment']
item = addRemove.object_with_id(pool_id).requestVdrContentUpdates(hardwareToAdd,hardwareToRemove,cloudsToAdd,cloudsToRemove)

pp item
```
