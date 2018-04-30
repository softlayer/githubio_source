---
title: "list_origin_mapping.rb"
description: "list_origin_mapping.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
# List all the origin pull mappings in the CDN.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/getOriginPullMappingInformation
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

cdn_id = 303_93

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
cdn_service = client['SoftLayer_Network_ContentDelivery_Account']

begin
  response = cdn_service.object_with_id(cdn_id).getOriginPullMappingInformation
  print response
rescue StandardError => exception
  puts "Unable to list origin mappings. : #{exception}"
end

```
