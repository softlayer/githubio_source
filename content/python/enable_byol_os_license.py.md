---
title: "enable_byol_os_license.py"
description: "enable_byol_os_license.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
Allow BYOL OS License

The script updates an image template to specify a user provided OS license, it allows you
to mark this image template as customer managed software license (BYOL).
It requires the image template identifier of a SoftLayer_Virtual_Guest_Block_Device_Template_Group type.

IMPORTANT: This property will work only for image templates created over servers provisioned with
RHEL 7.x Minimal installation specifically (https://knowledgelayer.softlayer.com/procedure/use-red-hat-cloud-access)

For more information please see below.

Import manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addByolAttribute

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The image template which you wish more details
imageTemplateId = 1797793

# Declaring the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
blockDeviceTemplateGroupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

try:
    # calling the addByolAttribute to enable user´s Os License, this will return a boolean.
    result = blockDeviceTemplateGroupService.addByolAttribute(id=imageTemplateId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to set OS License (BYOL) on image template: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
