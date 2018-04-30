---
title: "get_ordered_file_storage.rb"
description: "get_ordered_file_storage.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Storage"
tags:
    - "filestorage"
---


```
# Get the File Storage ordered.
#
# This script looks for the file storage we ordered
# using the order id to perform the research.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkStorage
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# The order id of our file storage
order_id = 5_505_803

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client.service_named('SoftLayer_Account')

# Declaring an object mask to get the order from the network storages
object_mask = 'mask[billingItem[orderItem[order]]]'

begin
  storages = account_service.object_mask(object_mask).getNetworkStorage
rescue StandardError => exception
  puts "Unable to retrieve the network storages. : #{exception}"
end

i = 0
while i < storages.length
  if storages[i]['billingItem']
    if storages[i]['billingItem']['orderItem']['order']['id'].to_i == order_id
      print 'The storage you ordered is: ' + storages[i]['id'].to_s
      break
    end
  end
  i += 1
end

```
