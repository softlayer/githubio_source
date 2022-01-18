---
title: "Attach and Detach a Block Device to a Virtual_Guest"
description: "Attaching and detaching secondary block devices on Virtual Guests"
date: "2016-08-22"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "attachdiskimage"
    - "detachdiskimage"
    - "getportablestoragevolumes"
    - "checkhostdiskavailability"
---

Attaching a currently detached portable block device to a given guest. The disk image will need to be migrated to the host the guest is on, so make sure to check if that host has enough disk space (with checkHostDiskAvailability) before attaching. This is only required for guests with local storage guests. SAN based guests don't need that step.

Running this on a disk that is already attached will move the disk to the new guest.

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new(:timeout => 120)
disk_id = 87654321
guest_id = 1234567

attach = client['SoftLayer_Virtual_Guest']
item = attach.object_with_id(guest_id).attachDiskImage(disk_id)

pp item
```

To detach the disk simply change `attachDiskImage(disk_id)` to `detachDiskImage(disk_id)`.
