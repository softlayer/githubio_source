---
title: "get_virtual_guest_billing_item.rb"
description: "get_virtual_guest_billing_item.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
tags:
    - "billing"
---


```
# Retrieve the billing items  for the VSIs in the account.
#
# This script makes a single call to the getVirtualGuests() method in the
# SoftLayer_Account API service and uses a object mask to get the
# billing items and items for each VSIs in the account.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key.
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the object mask to get information about the items
object_mask = 'mask[id, hostname, domain, datacenter[longName], billingItem[item]]'

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_account = client['SoftLayer_Account']

begin
  # Retrieve the VSIs billing items for the account.
  servers = hardware_account.object_mask(object_mask).getVirtualGuests
  print servers
rescue StandardError => exception
  puts "Unable to retrieve the VSIs. : #{exception}"
end

```
