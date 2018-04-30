---
title: "add_devices_to_pool.rb"
description: "add_devices_to_pool.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Bandwidth_Version"
    - "SoftLayer_Hardware_Server"
tags:
    - "bandwidthpools"
---


```
# Add servers and VSIs to a bandwidth pool.
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrContentUpdates
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

list_server_ips = ['173.192.220.104', '173.192.220.110']
list_vsi_ips = ['184.173.20.162']

pool_id = 151136

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(username: SL_API_USERNAME,
                                         api_key: SL_API_KEY)

hardware_service = softlayer_client.service_named('SoftLayer_Hardware_Server')
vsi_service = softlayer_client.service_named('SoftLayer_Virtual_Guest')
pool_service = softlayer_client.service_named('SoftLayer_Network_Bandwidth_Version1_Allotment')

begin
	hardware_to_add = []
	hardware_to_remove = []
	clouds_to_add = []
	clouds_to_remove = []
	list_server_ips.each do | ip |
		server = hardware_service.findByIpAddress(ip)
		hardware_to_add.push(server) 
	end
	list_vsi_ips.each do | ip |
		vsi = hardware_service.findByIpAddress(ip)
		clouds_to_add.push(vsi) 
	end
	result = pool_service.object_with_id(pool_id)
	                     .requestVdrContentUpdates(hardware_to_add, hardware_to_remove,
		                                             clouds_to_add, clouds_to_remove)
	ap result
rescue StandardError => e
  raise e
end

```
