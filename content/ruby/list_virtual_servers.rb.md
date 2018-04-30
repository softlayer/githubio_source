---
title: "list_virtual_servers.rb"
description: "list_virtual_servers.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "virtualservers"
---


```
# List all VSIs in your account.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Account
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']

# We will retrieve the additional information for each VSI:
# primaryIpAddress
# primaryBackendIpAddress
# datacenter
# datacenterName
# serviceProvider
# hardwareFunctionDescription
object_mask = 'mask[primaryIpAddress,primaryBackendIpAddress,datacenter,datacenterName,serviceProvider,hardwareFunctionDescription]'
account_service.setObjectMask(object_mask)

begin
  # getVirtualGuests() will get all the VSIs that an account has.
  result = accountService.getVirtualGuests
  pp result
rescue StandardError => exception
  puts "Unable to  get the VSIs: #{exception}"
end

```
