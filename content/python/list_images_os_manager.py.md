---
title: "list_images_os_manager.py"
description: "list_images_os_manager.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
List images templates

The script retrieves a list the images templates in the account,
it uses the ImageManager class.
For more information please see below.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Declare a new API service object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
imageManager = SoftLayer.ImageManager(client)

# Declare variables
object_mask = "mask[children[blockDevices[diskImage[softwareReferences[softwareDescription]]]]]"

try:
    result = imageManager.list_private_images(mask=object_mask)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to retrieve the image templates. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
