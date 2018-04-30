---
title: "get_regions.rb"
description: "get_regions.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location_Group"
tags:
    - "bandwidthpools"
---


```
# Get the valid regions to order a bandwidth pool.
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group
# http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group/getAllObjects
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group
# http://sldn.softlayer.com/article/Object-Filters
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

location_group_service = softlayer_client.service_named('SoftLayer_Location_Group')

filter = SoftLayer::ObjectFilter.new
filter.set_criteria_for_key_path('locationGroupType.name', operation: 'VDR')

begin
	regions = location_group_service.object_filter(filter)
	                                .getAllObjects
  ap regions     
rescue StandardError => e
  raise e
end

```
