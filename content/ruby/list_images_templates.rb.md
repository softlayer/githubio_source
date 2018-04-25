---
title: "list_images_templates.rb"
description: "list_images_templates.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```
# List all the private image templates in the account
#
# The script calls the SoftLayer_Account::getPrivateBlockDeviceTemplateGroups method
# to list the private templates in the account and uses an object mask
# to display more related information of the images templates
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
#
# License <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client.service_named('SoftLayer_Account')

# Declaring an object mask to get more information about the images templates
object_mask = 'mask[summary,note,status[name],storageRepository[datacenter],transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter],blockDevices[diskImage[type]]]]'

begin
  # Setting the object mask in the service and call the getPrivateBlockDeviceTemplateGroups to list the image templates
  result = account_service.object_mask(object_mask).getPrivateBlockDeviceTemplateGroups
  print result
rescue => error_reason
  puts "Unable to list the images templates #{error_reason}"
end

```
