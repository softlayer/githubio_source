---
title: "get_virtual_guests_of_dedicated_host.rb"
description: "get_virtual_guests_of_dedicated_host.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhosts"
---


```
# List associated guest of dedicated host.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_DedicatedHost/getGuests
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_virtual_guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Id of dedicated host you want to get virtual guests
dedicated_host_id = 9301

# Create a SoftLayer API client object
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
service = client['SoftLayer_Virtual_DedicatedHost']

begin
  # getGuest() will get all the virtual guests of dedicated hosts.
  virtual_guests = service.object_with_id(dedicated_host_id).getGuests

  virtual_guests.each do |guest|
    puts JSON.generate(guest)
  end

rescue StandardError => exception
  puts "Unable to get the virtual guests: #{exception}"
end

```
