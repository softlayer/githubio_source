---
title: "delete_image_template.rb"
description: "delete_image_template.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```
# Delete an image template
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
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
block_device_template_group_service = client.service_named('SoftLayer_Virtual_Guest_Block_Device_Template_Group')

# The image template which you wish to delete
image_template_id = 171_272

begin
  result = block_device_template_group_service.object_with_id(image_template_id).deleteObject
  print result
rescue => error_reason
  puts "Unable to delete the image #{error_reason}"
end

```
