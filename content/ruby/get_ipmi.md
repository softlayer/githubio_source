---
title: "Get IPMI info for BMS"
description: "Retrieve IPMI address, username, and password for all hardware on the account"
date: "2016-08-22"
classes:
  - "SoftLayer_Account"
tags:
  - "ipmi"
  - "dedicated"
  - "auth"
---

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

object_mask = 'mask[networkManagementIpAddress,remoteManagementAccounts[username,password],id,fullyQualifiedDomainName]'

item = client['SoftLayer_Account']
getIPMI = item.object_mask(object_mask).getHardware

pp getIPMI
```
