---
title: "get_servers_in_a_region.rb"
description: "get_servers_in_a_region.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "bandwidthpools"
---


```
# List the servers which belong to a region.
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

region_id = 1

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

account_service = softlayer_client.service_named('SoftLayer_Account')

filter = SoftLayer::ObjectFilter.new
filter.set_criteria_for_key_path('hardware.datacenter.groups.locationGroupTypeId', operation: region_id)

begin
	servers = account_service.object_filter(filter)
	                         .getHardware
  ap servers     
rescue StandardError => e
  raise e
end

```
