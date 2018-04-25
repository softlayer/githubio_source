---
title: "get_tags.rb"
description: "get_tags.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```
# Get all the tags in the account.
#
# The script gets all the tags in the account we make a simple
# call the getTags() in the SoftLayer_Account API service
#
# Important manual pages
# see http://sldn.softlayer.com/reference/services/SoftLayer_Account
# see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTags
#
# License <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key.
USERNAME = 'set me'
APIKEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: APIKEY)
account_service = client['SoftLayer_Account']

begin
  # Retrieving the tags list.
  servers = account_service.getTags
  print servers
rescue StandardError => exception
  puts "Unable to list the tags.  : #{exception}"
end

```
