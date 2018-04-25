---
title: "delete_image_template.py"
description: "delete_image_template.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
Delete an image template

The script makes a single call to the SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject
method to delete an image template. For more information see below.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

"""
The image template which you wish to delete
To get the list of images templates in your account 
call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
"""
imageTemplateId = 1796335

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
blockDeviceTemplateGroupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

try:
    # Calling the getObject to delete the image template
    result = blockDeviceTemplateGroupService.deleteObject(id=imageTemplateId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to delete the image template. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
