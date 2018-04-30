---
title: "get_create_object_options.rb"
description: "get_create_object_options.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Get the options to create VSIs.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest/getCreateObjectOptions
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
require 'softlayer_api'
require 'pp'

# Your SoftLayer username and API key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  # Getting all the options available to create VSIs
  options = virtual_guest_service.getCreateObjectOptions
  print options
rescue StandardError => exception
  puts "Unable to retrieve the options list to create VSIs. : #{exception}"
end

```
