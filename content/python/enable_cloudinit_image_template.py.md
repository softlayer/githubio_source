---
title: "enable_cloudinit_image_template.py"
description: "enable_cloudinit_image_template.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
Enable CloudInit

The script allows you to mark this image template as cloud init.
It requires the image template identifier of a SoftLayer_Virtual_Guest_Block_Device_Template_Group type.

ONLY virtual servers that were ordered without selecting additional software, post-provisioning scripts,
or advanced monitoring can be allowed to set cloudInit on their image templates.

For more information please see below.

Import manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addCloudInitAttribute

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# The image template which you wish more details
imageTemplateId = 1796623

# Declaring the API client
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
blockDeviceTemplateGroupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

try:
    # calling the addCloudInitAttribute to enable cloudInit, this will return a boolean.
    result = blockDeviceTemplateGroupService.addCloudInitAttribute(id=imageTemplateId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to set cloudInit on image template: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
