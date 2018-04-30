---
title: "gather_details_image_template.rb"
description: "gather_details_image_template.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```
# Get more details about the images templates.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject
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

# The image template which you wish more details
image_template_id = 171_272

# Declaring an object mask to get more information about the images templates
object_mask = 'mask[summary,note,status[name],storageRepository[datacenter],transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter],blockDevices[diskImage[type]]]]'

begin
  # Calling the getObject to get an instance of the image template
  result = block_device_template_group_service.object_mask(object_mask).object_with_id(image_template_id).getObject
  print result
rescue => error_reason
  puts "Unable to get the details #{error_reason}"
end

```
