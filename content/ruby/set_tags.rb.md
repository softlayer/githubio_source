---
title: "set_tags.rb"
description: "set_tags.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tag"
---


```
# Set tags for a VSI
#
# The script sets the tags for an arbitrary VSI,
# it makes a single call to the SoftLayer_Virtual_Guest::setTags method
# For more information please see below.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setTags
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer username and API key.
USERNAME = 'set me'
API_KEY = 'set me'

# The virtual guestId you wish to set the tags
id_virtual_guest = 784_498_4

# The tags you wish to set in the VSI
tags = 'mytag1, mytag2 ,mytag3, mytag4'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  # Sending the request to get the tags
  result = virtual_guest_service.object_with_id(id_virtual_guest).setTags(tags)
  print result
rescue StandardError => exception
  puts "Unable to set the tags. : #{exception}"
end

```
