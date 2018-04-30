---
title: "get_gateway_member_list.rb"
description: "get_gateway_member_list.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
tags:
    - "search"
---


```
# Get Gateway Member list using SoftLayer_Search::advancedSearch
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

filter_data = 'networkGatewayMemberFlag:1 _objectType:SoftLayer_Hardware'

begin
  # Display Gateway Member items same as Portal > Device List
  result = search_service.advancedSearch(filter_data)
  puts 'Process finished successfully'
  p result
rescue StandardError => e
  raise e
end

```
