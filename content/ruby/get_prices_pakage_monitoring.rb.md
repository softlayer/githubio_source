---
title: "get_prices_pakage_monitoring.rb"
description: "get_prices_pakage_monitoring.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item"
    - "SoftLayer_Product_Package"
tags:
    - "monitoring"
---


```
# Get the prices for order a Monitor package
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The package Id for Monitoring package
package_id = 0

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
package_service = client.service_named('SoftLayer_Product_Package')

# Add an object mask to retrieve our package's related items such as its
# prices, attributes, etc for more information see
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item
object_mask = 'mask[attributes[attributeTypeKeyName],itemCategory,prices[bundleReferences[bundleItem],categories,attributes[itemPriceAttributeType]]]'

begin
  # Get the prices
  # You can filter more the data only to display the data related to monitoring_package
  # by adding a filter to show only the data where the categoryCode = monitoring_package.
  # Also you can filter more the data only to display the data related to firewalls
  # by adding a filter to show only the data where the categoryCode = vlan_firewall
  prices = package_service.object_with_id(package_id).object_mask(object_mask).getItems
  puts prices
rescue StandardError => exception
  puts "Unable to get the prices: #{exception}"
end

```
