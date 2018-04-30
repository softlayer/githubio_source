---
title: "get_available_package_for_image.py"
description: "get_available_package_for_image.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "package"
---


```
"""
Get available package for an image template

This script retrieves a collection of valid locations for this package

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getAvailablePackagesForImageTemplate
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

# So we can talk to the SoftLayer API:
import SoftLayer
import json

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'
# Declare the image template id
imageTemplateId = 429428
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Build a SoftLayer_VIrtual_Guest_Block_Device_Template_Group object
imageTemplate = {
                "id": imageTemplateId
                }
try:
    packages = client['SoftLayer_Product_Package'].getAvailablePackagesForImageTemplate(imageTemplate)
    print(json.dumps(packages, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get available packages for an image faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
