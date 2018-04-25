---
title: "list_server.rb"
description: "list_server.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```
# List Bare Metal servers.
#
# The script lists all the bare metal server in your account,
# it makes a single call to the SoftLayer_Account::getHardware method.
# For more information please see below.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Account
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware/getHardware
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']

# We will retrieve the additional information
# for each server:
# primaryIpAddress
# primaryBackendIpAddress
# datacenter
# datacenterName
# serviceProvider
# hardwareFunctionDescription
object_mask = 'mask[primaryIpAddress,primaryBackendIpAddress,datacenter,datacenterName,serviceProvider,hardwareFunctionDescription]'
account_service.setObjectMask(object_mask)

begin
  # getHardware() will get all the bare metal servers that an account has.
  result = account_service.getHardware
  pp result
rescue StandardError => exception
  puts "Unable to  get the servers: #{exception}"
end

```
