---
title: "unshare_image_template.py"
description: "unshare_image_template.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
Un-share an image template

The script un-shares an image template it makes a call to
SoftLayer_Virtual_Guest_Block_Device_Template_Group::denySharingAccess method,
For more information please see below:

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess
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
The image template which you wish to unshare
To get the list of images templates in your account 
call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
"""
imageTemplateId = 1796405

# The account you wish to unshare the image template
accountToUnshare = 207819

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
blockDeviceTemplateGroupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

try:
    # Calling the denySharingAccess method to ushare the image template
    result = blockDeviceTemplateGroupService.denySharingAccess(accountToUnshare, id=imageTemplateId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to unshare the image template. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
