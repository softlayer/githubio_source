---
title: "search_tag.rb"
description: "search_tag.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "tag"
---


```
# Search VSI by tag
#
# The script retrieves all the VSIs which contain an
# arbitrary list of tags
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer username and API key.
USERNAME = 'set me'
API_KEY = 'set me'

# list of tags to look for
tags = %w(tag1 tag2)

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']

# Declaring an object filter to get only the virtual servers which contains the tags that we are looking for
object_filter = SoftLayer::ObjectFilter.new
object_filter.set_criteria_for_key_path('virtualGuests.tagReferences.tag.name',           'operation' => 'in',
                                                                                          'options' => [{
                                                                                            'name' => 'data',
                                                                                            'value' => tags
                                                                                          }])

begin
  # Sending the request to get the virtual guest using the filter
  result = account_service.object_filter(object_filter).getVirtualGuests
  print result
rescue StandardError => exception
  puts "Unable to retrieve the virtual guests. : #{exception}"
end

```
