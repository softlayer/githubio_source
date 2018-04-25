---
title: "retrieve_metadata.rb"
description: "retrieve_metadata.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```
# Retrieves the user data for the VSIs in the account.
#
# The script gets the user metadata for a VSI in the account we make a simple
# call the getVirtualGuests() in the SoftLayer_Virtual_Guest API service
# and we set an object mask to get the information about the user data.
#
# Important manual pages
# see http://sldn.softlayer.com/reference/services/SoftLayer_Account
# see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
#
# License <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
APIKEY = 'set me'

# Adding the object mask to the call to get the information about the user data.
object_mask = 'mask[userData]'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: APIKEY)
account_service = client['SoftLayer_Account']

begin
  # Retrieving our account's VSIs records.
  servers = account_service.object_mask(object_mask).getVirtualGuests
  print servers
rescue StandardError => exception
  puts "Unable to retrieve the VSI list. : #{exception}"
end

```
