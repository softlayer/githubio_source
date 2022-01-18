---
title: "Create a snapshot schedule"
description: "Create a snapshot schedule for Endurance storage."
date: "2016-08-23"
classes: ["SoftLayer_Network_Storage"]
tags:
    - "enablesnapshots"
    - "blockstorage"
---

This method is not valid for Legacy iSCSI Storage Volumes. You need to have already purchased snapshot space for the script to work properly.

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new(:timeout => 120)

storageId = 11657445

# Define parameters for snapshot
scheduleType = 'WEEKLY'
retentionCount = '20'
minute = '1'
hour = '13'
dayOfWeek = 'SUNDAY'

snap = client['SoftLayer_Network_Storage']
enable = snap.object_with_id(storageId).enableSnapshots(scheduleType, retentionCount, minute, hour, dayOfWeek)
pp enable 
```
