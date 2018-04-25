---
title: "share_image_template.rb"
description: "share_image_template.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```
# Share an image template to another Softlayer account
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
#
# License <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
block_device_template_group_service = client.service_named('SoftLayer_Virtual_Guest_Block_Device_Template_Group')

# The image template which you wish to share
# To get the list of images templates in your account call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
image_template_id = 315_894

# The account you wish to share the image template
account_to_share = 207_819

begin
  # Calling the permitSharingAccess method to share the image template
  result = block_device_template_group_service.object_with_id(image_template_id).permitSharingAccess(account_to_share)
  print result
rescue => error_reason
  puts "Unable to share the image template #{error_reason}"
end

```
