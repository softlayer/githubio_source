---
title: "get_billing_info.rb"
description: "get_billing_info.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Info"
    - "SoftLayer_Account"
tags:
    - "billing"
---


```
# Retrieve the billing info for the Bare Metals in the account.
#
# This script makes a single call to the getHardware() method in the
# SoftLayer_Account API service and uses a object mask to get the
# billing info for each Bare Metal server in the account.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Info
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the object mask to get information about the billing item.
object_mask = 'mask[id, hostname, domain, datacenter[longName], billingItem[recurringFee]]'

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_account = client['SoftLayer_Account']

begin
  # Retrieve the bare metal servers for the account.
  servers = hardware_account.object_mask(object_mask).getHardware
  print servers
rescue StandardError => exception
  puts "Unable to retrieve the servers. : #{exception}"
end

```
