---
title: "remove_devices_from_pool.rb"
description: "remove_devices_from_pool.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Bandwidth_Version"
    - "SoftLayer_Hardware_Server"
tags:
    - "bandwidthpools"
---


```
# Remove servers and VSIs from a bandwidth pool.
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

list_server_ips = ['184.172.45.210', '108.168.251.167']
list_vsi_ips = ['169.54.234.102']

pool_id = 234419

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
  list_server_ips.each do |ip|
    server = hardware_service.findByIpAddress(ip)
    hardware_to_remove.push(server)
  end
  list_vsi_ips.each do |ip|
    vsi = vsi_service.findByIpAddress(ip)
    clouds_to_remove.push(vsi)
  end
  result = pool_service.object_with_id(pool_id)
                       .requestVdrContentUpdates(hardware_to_add, hardware_to_remove,
                                                 clouds_to_add, clouds_to_remove)
  p result
rescue StandardError => e
  raise e
end

```
