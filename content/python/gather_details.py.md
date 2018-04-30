---
title: "gather_details.py"
description: "gather_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
Get image template details.

The script gets more details of an arbitrary image template,
it uses an object mask to retrieve the information.
For more information please see below.

Import manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject

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
imageTemplateId = 1796405

# Declaring the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
blockDeviceTemplateGroupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

# Declaring an object mask to get more information about the images templates
objectMask = "mask[summary,note,status[name],storageRepository[datacenter]," \
             "transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter]," \
             "blockDevices[diskImage[type]]]]"

try:
    # calling the getObject to get an instance of the image template
    result = blockDeviceTemplateGroupService.getObject(mask=objectMask, id=imageTemplateId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to get the details. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
