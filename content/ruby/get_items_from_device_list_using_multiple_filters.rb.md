---
title: "get_items_from_device_list_using_multiple_filters.rb"
description: "get_items_from_device_list_using_multiple_filters.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
tags:
    - "search"
---


```
# Get items from "Portal>Device List" filtered by multiple filters
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

# Setting some Filters:
# Devicename: mydevice.softlayer.local
#     Location: Dallas 6
#     Devicetype: Gateway Member
#     PrivateIp: 10.107.141.195
private_ip = '10.107.141.195'
location = 'Dallas 6'
device_name = 'mydevice.softlayer.local'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY,
                                         endpoint_url: API_PUBLIC_ENDPOINT)

search_service = softlayer_client.service_named('SoftLayer_Search')

filter_data = "networkGatewayMemberFlag:\"1\" & "\
              "datacenter.longName:\"#{location}\" & "\
              "primaryBackendIpAddress:#{private_ip} & "\
              "fullyQualifiedDomainName:#{device_name} "\
              '_objectType:SoftLayer_Hardware'

begin
  # Display items as "Portal>Device List" filtered by multiple filters
  result = search_service.advancedSearch(filter_data)
  puts 'Process finished successfully'
  p result
rescue StandardError => e
  raise e
end

```
