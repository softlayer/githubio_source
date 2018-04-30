---
title: "migrate_vsi_to_another_dedicated_host.rb"
description: "migrate_vsi_to_another_dedicated_host.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "dedicatedhosts"
---


```
# Create a transaction to migrate an instance from one dedicated host to another dedicated host.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/migrateDedicatedHost
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

vsi_id_to_migrate = 37117661
dedicated_host_target = 10009

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
service = client['SoftLayer_Virtual_Guest']

begin
  # Create the transaction to migrate the vsi to another dedicated host.
  response = service.object_with_id(vsi_id_to_migrate).migrateDedicatedHost dedicated_host_target

  puts "Transaction to migrate vsi was created: #{response}"

rescue StandardError => exception
  puts "Unable to place order: #{exception}"
end
```
