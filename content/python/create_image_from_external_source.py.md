---
title: "create_image_from_external_source.py"
description: "create_image_from_external_source.py"
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
Create Image Template from external source

This script creates a transaction to import a disk image from an external source and create 
a standard image template

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Declare the group name to be applied to the imported template
name = 'imageTemplateTest'
# Declare the note to be applied to the imported template
note = 'An optional note'

'''
Declare referenceCode of the operating system software description for the imported VHD
available options: CENTOS_6_32, CENTOS_6_64, CENTOS_7_64, REDHAT_6_32, REDHAT_6_64, REDHAT_7_64, 
UBUNTU_12_32, UBUNTU_12_64, UBUNTU_14_32, UBUNTU_14_64, WIN_2003-STD-SP2-5_32, WIN_2003-STD-SP2-5_64, 
WIN_2008-STD-R2-SP1_64, WIN_2012-STD_64.
'''
operatingSystemReferenceCode = 'CENTOS_6_64'

'''
Define the parameters below, which refers to object storage where the image template is stored. 
It will help to build the uri.
'''
# Declare the object storage account name
objectStorageAccountName = 'SLOS307608-10'
# Declare the cluster name where the image is stored
clusterName = 'dal05'
# Declare the container name where the image is stored
containerName = 'OS'
# Declare the file name of the image stored in the object storage, it should be .vhd or 
fileName = 'testImage2.vhd-0.vhd'

"""
Creating an SoftLayer_Container_Virtual_Guest_block_Device_Template_Configuration Skeleton
which contains the information from external source
"""
configuration = {
    'name': name,
    'note': note,
    'operatingSystemReferenceCode': operatingSystemReferenceCode,
    'uri': 'swift://' + objectStorageAccountName + '@' + clusterName + '/' + containerName + '/' + fileName
}

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
groupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

try:
    result = groupService.createFromExternalSource(configuration)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the image template from external source: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
