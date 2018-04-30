---
title: "list_images_templates.py"
description: "list_images_templates.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "images-templates"
---


```
"""
Get private image template

the script calls the SoftLayer_Account::getPrivateBlockDeviceTemplateGroups method
to list the private templates in the account and uses an object mask
to display more related information of the images templates

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups
http://sldn.softlayer.com/reference/dataypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# declaring an object mask to get more information about the images templates
objectMask = "mask[summary,note,status[name],storageRepository[datacenter]," \
             "transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter]," \
             "blockDevices[diskImage[type]]]]"

try:
    result = accountService.getPrivateBlockDeviceTemplateGroups(mask=objectMask)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to retrieve the list of image templates. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
