---
title: "create_image_template_standard.rb"
description: "create_image_template_standard.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Block_Device"
tags:
    - "imagetemplates"
---


```
# Create standard image template.
#
# The example creates a standard image template from a CCI
# which contains 3 disk. for more information see below.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'
ENDPOINT = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY, endpoint_url: ENDPOINT)
virtual_guest_service = client.service_named('SoftLayer_Virtual_Guest')

# Build a skeleton SoftLayer_Virtual_Guest_Block_Device object
# containing the disk which will be in the image template
# It is not necessary to specify all disks in the virtual server
# only is required specify the first disk.
# To get the list of block devices in the Virtual Guest
# call the SoftLayer_Virtual_Guest::getBlockDevices method
block_devices_template = [
  {
    'id' => 802_015_8
  },
  {
    'id' => 919_679_0
  },
  {
    'id' => 928_982_8
  }
]

group_name = 'the name for the template'
note = 'an optional note'

# The virtual guest ID of the virtual server from you want
# to take the image template.
# To get a list of all your virtual servers in your account
# use the Softlayer::getVirtualGuests method
virtual_guest_id = 614_303_8

begin
  result = virtual_guest_service.object_with_id(virtual_guest_id).createArchiveTransaction(group_name, block_devices_template, note)
  print result
rescue => error_reason
  puts "Unable to create the image #{error_reason}"
end

```
