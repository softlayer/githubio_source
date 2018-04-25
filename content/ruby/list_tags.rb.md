---
title: "list_tags.rb"
description: "list_tags.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tag"
---


```
# List the tags for a VSI
#
# The scripts list all the tags set in an arbitrary  VSI,
# it uses the SoftLayer_Virtual_Guest::getTagReferences method
# to get the tags. For more information please see below
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getTagReferences
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer username and API key.
USERNAME = 'set me'
API_KEY = 'set me'

# The virtual guestId you wish to get the tags
virtual_guest_id = 784_498_4

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  # Sending the request to get the tags
  result = virtual_guest_service.object_with_id(virtual_guest_id).getTagReferences
  print result
rescue StandardError => exception
  puts "Unable retrieve the tags. : #{exception}"
end

```
