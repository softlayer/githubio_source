---
title: "get_netscaler_list.rb"
description: "get_netscaler_list.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller"
    - "SoftLayer_Search"
tags:
    - "search"
---


```
# Get Netscaler list using SoftLayer_Search::advancedSearch
#
# Important manual pages:
# see http://sldn.softlayer.com/reference/services/SoftLayer_Search/advancedSearch
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

# Softlayer API public endpoint
API_PUBLIC_ENDPOINT = 'https://api.softlayer.com/xmlrpc/v3.1/'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY,
                                         endpoint_url: API_PUBLIC_ENDPOINT)

search_service = softlayer_client.service_named('SoftLayer_Search')

filter_data = '_objectType:SoftLayer_Network_Application_Delivery_Controller'

begin
  # Display Netscaler items same as Portal > Device List
  result = search_service.advancedSearch(filter_data)
  puts 'Process finished successfully'
  p result
rescue StandardError => e
  raise e
end

```
