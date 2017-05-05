---
title: "Get Virtual Console Virtual Guest"
description: "Retrieve the IP, username, and password needed to access the KVM console for a Virtual Guest."
date: "2017-05-04"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "getObject"
---


```ruby
=begin
@author Ryan Tiffany
=end

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)
virtual_server_id = 31678643

mask = 'mask[consoleIpAddressRecord[ipAddress[ipAddress],port],operatingSystem[passwords]]'

getDetails = client['SoftLayer_Virtual_Guest'].object_mask(mask).object_with_id(virtual_server_id).getObject
pp getDetails
```
