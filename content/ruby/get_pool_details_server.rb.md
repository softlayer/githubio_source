---
title: "get_pool_details_server.rb"
description: "get_pool_details_server.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "bandwidthpools"
---


```
# Get the details for a bandwidth pool (list only the servers).
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

pool_id = 115045

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

account_service = softlayer_client.service_named('SoftLayer_Account')

mask = 'mask(SoftLayer_Hardware_Server)[projectedPublicBandwidthUsage, datacenter, outboundPublicBandwidthUsage, bandwidthAllocation, virtualRackId]'

filter = SoftLayer::ObjectFilter.new
filter.set_criteria_for_key_path('hardware.virtualRackId', operation: pool_id)

begin
	details = []
	servers = account_service.object_mask(mask)
	                         .object_filter(filter)
	                         .getHardware
                         
  servers.each do |server|
  	detail = {}
  	detail[:server] = server['fullyQualifiedDomainName']	
  	detail[:ip] = server['primaryIpAddress']
   	detail[:location] = server['datacenter']['longName']
    detail[:allocation] = ((server['bandwidthAllocation']).to_f / 1000).to_s + ' TB'
    detail[:currentUsage] = ((server['outboundPublicBandwidthUsage']).to_f * 1000).to_s + ' MB'
    detail[:projectedUsage] = ((server['projectedPublicBandwidthUsage']).to_f * 1000).to_s + ' MB'    
    details.push(detail)
  end
  ap details     
rescue StandardError => e
  raise e
end

```
