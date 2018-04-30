---
title: "create_pool.rb"
description: "create_pool.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
---


```
# Create a bandwidth pool.
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

template = {
	accountId: 207819,
	bandwidthAllotmentTypeId: 2,
	locationGroupId: 1,  # The region for the pool.
	name: 'test_pool_api'
}

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

bandwidth_service = softlayer_client.service_named('SoftLayer_Network_Bandwidth_Version1_Allotment')

begin
	result = bandwidth_service.createObject(template)
	ap result
rescue StandardError => e
  raise e
end

```
