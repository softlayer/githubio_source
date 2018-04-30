---
title: "list_bandwidth_pools.rb"
description: "list_bandwidth_pools.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
---


```
# List the bandwidth pools in the account.
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getBandwidthAllotments
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment
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

mask = 'mask[id, name, serviceProviderId, locationGroup[name], locationGroup,'\
       ' hardwareCount, privateNetworkOnlyHardwareCount, virtualGuestCount,'\
       ' bareMetalInstanceCount, applicationDeliveryControllerCount,'\
       ' totalBandwidthAllocated, outboundPublicBandwidthUsage,'\
       ' bandwidthAllotmentTypeId, projectedPublicBandwidthUsage]'

filter = SoftLayer::ObjectFilter.new
filter.set_criteria_for_key_path('bandwidthAllotments.bandwidthAllotmentTypeId', operation: '!= 1')

begin
  pools = []
	data = account_service.object_mask(mask)
	                      .object_filter(filter)
	                      .getBandwidthAllotments                     
  data.each do |item|
    pool = {}    
    pool[:name] = item['name']
    if item['locationGroup']
      pool[:region] = item['locationGroup']['name'] 
    else
      pool[:region] = 'NA'
    end
    pool[:allocation] = (item['totalBandwidthAllocated'] / 1000).to_s + ' TB'    
    if item['outboundPublicBandwidthUsage']
      pool[:currentUssage] = (item['outboundPublicBandwidthUsage'] * 1000).to_s + ' MB'
    else
      pool[:currentUssage] = '0 MB'
    end
    if item['projectedPublicBandwidthUsage']
      pool[:projectableUsage] = (item['projectedPublicBandwidthUsage'] * 1000).to_s + ' MB'
    else
      pool[:projectableUsage] = '0 MB'
    end
    pools.push(pool)
  end
  ap pools     
rescue StandardError => e
  raise e
end

```
