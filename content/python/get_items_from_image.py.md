---
title: "get_items_from_image.py"
description: "get_items_from_image.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Grouo"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "package"
---


```
"""
Get items from an image template

This script returns a collection of SoftLayer_Product_Item objects from a
SoftLayer_Virtual_Guest_Block_Device_Template_Grouo object

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemsFromImageTemplate
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/

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
# Declare a Package Id for which you want to get its items
packageId = 46
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
# Build a SoftLayer_VIrtual_Guest_Block_Device_Template_Group object
imageTemplate = {
                "id": imageTemplateId
                }
try:
    items = client['SoftLayer_Product_Package'].getItemsFromImageTemplate(imageTemplate, id=packageId)
    print(json.dumps(items, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get items from the image template faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
