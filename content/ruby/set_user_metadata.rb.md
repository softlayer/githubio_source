---
title: "set_user_metadata.rb"
description: "set_user_metadata.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "metadata"
---


```
# Set the user data for a VSI.
#
# The script sets the user metadata for a VSI we make a simple
# call the setUserMetadata() in the SoftLayer_Virtual_Guest API service
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setUserMetadata
#
# License <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
APIKEY = 'set me'

# The user data you wish to set
user_data = ['this is my user data']

# The id of the VSI where you want to set the user data
virtual_guest_id = 737_050_2

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: APIKEY)
virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  # Setting the user metadata.
  result = virtual_guest_service.object_with_id(virtual_guest_id).setUserMetadata(user_data)
  print result
rescue StandardError => exception
  puts "Unable to set the user metadata. : #{exception}"
end

```
