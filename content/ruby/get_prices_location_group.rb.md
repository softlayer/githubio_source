---
title: "get_prices_location_group.rb"
description: "get_prices_location_group.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "filestorage"
---


```
# Get prices for File Storage
#
# The script retrieves the items and prices to order a File Storage
# and uses filters to get the prices for an arbitrary location group
# and an arbitrary item description.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems
# http://sldn.softlayer.com/article/Object-Filters
# http://sldn.softlayer.com/article/Object-Masks
# http://sldn.softlayer.com/blog/cmporter/Location-based-Pricing-and-You
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The package for File Storage
package = 222

# The list of location groups you wish to filter in order to show only
# the prices which belong to those location groups for example we only
# list the prices which locationGroupId is 503 whose prices are valid
# in the locations:   "Toronto 1", "Amsterdam 3", "Montreal 1"
# and "Amsterdam 1"
location_groups_ids = [503]

# The description of the item you wish to get its prices
item_description = '20 GB Storage Space'

client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, timeout: 600)
package_service = client.service_named('SoftLayer_Product_Package')

# We are setting a filter to get only the items which description
# contains "20 GB Storage Space"
object_filter = SoftLayer::ObjectFilter.new do |object_filter|
  object_filter.accept('items.description').when_it contains(item_description)
end

# We are adding to our filter the locationGroups we wish to see in the result
object_filter.set_criteria_for_key_path('items.prices.locationGroupId',           'operation' => 'in',
                                                                                  'options' => [{
                                                                                    'name' => 'data',
                                                                                    'value' => location_groups_ids
                                                                                  }])

# We are creating an object mask in order to see more details in the result
# in this case we are going to see the details of the locationGroup.
object_mask = 'mask[prices[pricingLocationGroup[locations[id, name, longName]]]]'

begin
  result = package_service.object_with_id(package).object_filter(object_filter).object_mask(object_mask).getItems
  puts JSON.pretty_generate(result)
rescue StandardException => exception
  puts "Unable to get the items.  #{exception}"
end

```
