---
title: "Toggle cloudinit on an image template"
description: "Toggle cloudinit on an image template"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
Disable CloudInit

The script allows you to disable this image template as cloud init.
It requires the image template identifier of a SoftLayer_Virtual_Guest_Block_Device_Template_Group type.
For more information please see below.

Import manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteCloudInitAttribute

"""

import SoftLayer

from pprint import pprint as pp

# The image template which you wish more details
imageTemplateId = 1796623

# Declaring the API client
client = SoftLayer.create_client_from_env()
blockDeviceTemplateGroupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

try:
    # calling the deleteCloudInitAttribute to disable cloudInit, this will return a boolean.

    # DISABLE
    result = blockDeviceTemplateGroupService.deleteCloudInitAttribute(
        id=imageTemplateId)

    # ENABLE
    result = blockDeviceTemplateGroupService.addCloudInitAttribute(
        id=imageTemplateId)

    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to delete cloudInit on image template: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
