---
title: "Create Storage Snapshot"
description: "Initiate a manual snapshot of an Endurance or Performance Block storage volume."
date: "2016-08-11"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
    - "iscsi"
    - "blockStorage"
    - "objectMask"
---

Trigger a manual snapshot creation of a Block storage volume.

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
network_storage_id = 1234567
client = SoftLayer::Client.new(:timeout => 120)

createsnap = client[:Network_Storage_Iscsi].object_with_id(network_storage_id).createSnapshot
pp createsnap
```

The process can take sometime to complete. You can check the snapshots associated with a storage volume by using the code below:

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
network_storage_id = 1234567
client = SoftLayer::Client.new(:timeout => 120)

snapshots = client[:Network_Storage_Iscsi].object_with_id(network_storage_id).getSnapshotsForVolume
pp snapshots
```
