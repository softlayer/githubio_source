---
title: "get_bandwidth_data.rb"
description: "get_bandwidth_data.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
# Get bandwidth data in a CDN.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthData
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

cdn_id = 303_93

start_date = '2014-10-10 00:00:00'
end_date = '2015-10-10 05:00:00'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
cdn_service = client['SoftLayer_Network_ContentDelivery_Account']

begin
  response = cdn_service.object_with_id(cdn_id).getBandwidthData(start_date, end_date)
  print response
rescue StandardError => exception
  puts "Unable to get the bandwidth data. : #{exception}"
end

```
