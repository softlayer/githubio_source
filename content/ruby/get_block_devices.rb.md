---
title: "get_block_devices.rb"
description: "get_block_devices.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Block_Device"
tags:
    - "virtualservers"
---


```
# Retrieve a computing instance's block devices. Block devices link disk images to computing instances.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getBlockDevices
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

virtual_guest_id = 6032256

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  virtual_guest_block_device = virtual_guest_service.object_with_id(virtual_guest_id)
                                                    .getBlockDevices
  ap virtual_guest_block_device
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
