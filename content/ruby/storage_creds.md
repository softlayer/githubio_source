---
title: "Get storage credentials for Block Storage"
description: "Retrieving the username and password for Performance/Endurance Block storage"

date: "2016-08-08"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
  - "objectmask"
  - "blockstorage"
  - "getobject"
---

The following script allows you retrieve the username and password for Performance/Endurance Block storage if you have authorized hosts against the storage.

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
network_storage_id = 1234567
client = SoftLayer::Client.new(:timeout => 120)
account_service = client['SoftLayer_Network_Storage_Iscsi']
object_mask = 'mask[allowedHardware[allowedHost[credential]],allowedVirtualGuests[allowedHost[credential]]]'
item = account_service.object_mask(object_mask).object_with_id(network_storage_id).getObject

pp item
```
