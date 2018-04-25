---
title: "copy_to_external_source.py"
description: "copy_to_external_source.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Container_Virtual_Guest_"
tags:
    - "images-templates"
---


```
"""
Copy to external source

This script creates a transaction to export/copy a template to an external source

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToExternalSource
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Declare the image template identifier that you wish to export
imageTemplateId = 1796405

'''
Define the parameters below, which refers to object storage where the image template will be copied.
It will help to build the uri.
'''
# Declare the object storage account name
objectStorageAccountName = 'SLOS307608-10'
# Declare the cluster name where the image will be copied
clusterName = 'dal05'
# Declare the container name where the image will be copied
containerName = 'OS'
# Declare the file name of the image stored in the object storage, it should be .vhd or 
fileName = 'testImage4f.iso'

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
groupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

"""
Creating an SoftLayer_Container_Virtual_Guest_block_Device_Template_Configuration Skeleton
"""
configuration = {
    'uri': 'swift://' + objectStorageAccountName + '@' + clusterName + '/' + containerName + '/' + fileName
}

try:
    result = groupService.copyToExternalSource(configuration, id=imageTemplateId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print('Unable to copy: \nfaultCode= %s, \nfaultString= %s'
          % (e.faultCode, e.faultString))
    exit(1)

```
