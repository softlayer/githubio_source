---
title: "get_hardware_location.rb"
description: "get_hardware_location.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```
#
# Get location for your Bare Metal Servers.
#
# The script retrieves the location for all your bare metal servers
# in your account. For more information see below:
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware/getLocation
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer username and API key.
USERNAME = '-'
API_KEY = 'apikey_goes_here'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']
hardware_service = client['SoftLayer_Hardware']

begin
  # Getting all the bare metal servers in your account.
  servers = account_service.getHardware
  servers.each do |server|
    # Calling the getLocation() for each bare metal in your account
    print server['id']
    location = hardware_service.object_with_id(server['id']).getLocation
    print 'server name: ' + server['hostname'] + 'location: '
    print location
  end
rescue StandardError => exception
  puts "Unable to retrieve the Bare metal list. : #{exception}"
end

```
