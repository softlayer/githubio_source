---
title: "get_items_filtered_by_private_ip.rb"
description: "get_items_filtered_by_private_ip.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Vlan_Firewall"
tags:
    - "search"
---


```
# Get items from "Portal>Device List" filtered by Private IP
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

private_ip = '10.102.52.131'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY,
                                         endpoint_url: API_PUBLIC_ENDPOINT)

search_service = softlayer_client.service_named('SoftLayer_Search')

filter_data = "primaryBackendIpAddress:#{private_ip} "\
              '_objectType:SoftLayer_Hardware,'\
              'SoftLayer_Virtual_Guest,'\
              'SoftLayer_Network_Vlan_Firewall,'\
              'SoftLayer_Network_Application_Delivery_Controller'

begin
  # Display items as "Portal>Device List" filtered by Private IP
  result = search_service.advancedSearch(filter_data)
  puts 'Process finished successfully'
  p result
rescue StandardError => e
  raise e
end

```
