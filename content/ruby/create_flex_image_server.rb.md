---
title: "create_flex_image_server.rb"
description: "create_flex_image_server.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Disk_Image_Capture_Template"
tags:
    - "imagetemplates"
---


```
# Create an flex image from a Server
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/captureImage
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
#
# License <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_server_service = client.service_named('SoftLayer_Hardware_Server')

# The virtual hardware ID of the machine you wish to create the image template
hardware_server_id = 743_897_2

# Creating an SoftLayer_Container_Disk_Image_Capture_Template Skeleton
# wich contains the information for our flex image
capture_template = {
  'complexType' => 'SoftLayer_Container_Disk_Image_Capture_Template',
  'description' => 'test',
  'name' => 'reloadFlexImage',
  'summary' => 'test summary'
}

begin
  # Calling the captureImage method along with our captureTemplate to create the flexImage
  result = hardware_server_service.object_with_id(hardware_server_id).captureImage(capture_template)
  print result
rescue => error_reason
  puts "Unable to create the image #{error_reason}"
end

```
