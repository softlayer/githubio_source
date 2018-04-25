---
title: "delete_origin_mapping.rb"
description: "delete_origin_mapping.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping"
tags:
    - "cdn"
---


```
# Delete an origin mappings in a CDN.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/deleteOriginPullRule
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

cdn_id = 303_93
origin_id = 'op907521'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
cdn_service = client['SoftLayer_Network_ContentDelivery_Account']

begin
  response = cdn_service.object_with_id(cdn_id).deleteOriginPullRule(origin_id)
  print response
rescue StandardError => exception
  puts "Unable to delete the origin mappings. : #{exception}"
end

```
