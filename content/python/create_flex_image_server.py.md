---
title: "create_flex_image_server.py"
description: "create_flex_image_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Disk_Image_Capture_Template"
tags:
    - "images-templates"
---


```
"""
Create an flex image from a Server

The script makes a single call to the SoftLayer_Hardware_Server::captureTemplate
method in order to create a flex image from the bare metal server.
For more information please see below.

IMPORTANT: This script will no longer work properly as of Monday August 7,
2017 IBM Cloud (formerly SoftLayer) has discontinued offering the Flex Image service.
https://control.softlayer.com/support/event/details/46488623

Important manual page:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/captureImage
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# The hardware server ID of the machine you wish to create the image template
hardwareServerId = 7438972

"""
Creating an SoftLayer_Container_Disk_Image_Capture_Template Skeleton
which contains the information for our flex image
"""
captureTemplate = {
    "complexType": "SoftLayer_Container_Disk_Image_Capture_Template",
    "description": "test",
    "name": "reloadFlexImage",
    "summary": "test summary",
}

"""
Declare the API client
client = SoftLayer.Client(endpoint_url=ENDPOINT, username=USERNAME,api_key=API_KEY)
"""
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareServerService = client['SoftLayer_Hardware_Server']

try:
    # calling the captureImage method along with our captureTemplate to create the flexImage
    result = hardwareServerService.captureImage(captureTemplate, id=hardwareServerId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the image template. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
