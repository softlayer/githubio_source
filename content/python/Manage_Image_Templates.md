---
title: "Managing Image Templates"
description: "A variety of examples on how to work with Image Templates, aka SoftLayer_Virtual_Guest_Block_Device_Template_Group"
date: "2020-06-25"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Location"
tags:
    - "imagetemplate"
    - "template"
---

## Create an Image Template

The script creates a standard image template, it makes
a call to the [SoftLayer_Virtual_Guest::createArchiveTransaction](/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction) method
sending the IDs of the disks in the request, the response will provide an ID property which is the Transaction number until the template has been created. 
This will take the Virtual Guest offline for this process.


```python
import SoftLayer
from pprint import pprint as pp


# The virtual guest ID you want to create a template
virtualGuestId = 39202937
# The name of the image template
groupName = 'fmirGroupImageTemplate'
# An optional note for the image template
note = 'an optional fmir note'

"""
Build a skeleton SoftLayer_Virtual_Guest_Block_Device object
containing the disks you want to the image.
In this case we are going take an image template of 2 disks
from the virtual machine.
"""
blockDevices = [
    {"id": 60788837},  # "complexType": "SoftLayer_Virtual_Guest_Block_Device"
    {"id": 59411427},  # "complexType": "SoftLayer_Virtual_Guest_Block_Device"
]

# Declare a new API service object
client = SoftLayer.create_client_from_env()

try:
    # Creating the transaction for the image template
    response = client.call(
        'SoftLayer_Virtual_Guest', 
        'createArchiveTransaction',
        groupName,
        blockDevices,
        note,
        id=virtualGuestId)
    pp(response)
except SoftLayer.SoftLayerAPIError as e:
    """
    # Handle or Print the SoftLayer error if there was one.
    """
    print("Unable to create the image template. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

## List Image Templates

### Using the python manager
```python
import SoftLayer
from pprint import pprint as pp

# Declare a new API service object
client = SoftLayer.create_client_from_env()
imageManager = SoftLayer.ImageManager(client)

# Declare variables
object_mask = "mask[children[blockDevices[diskImage[softwareReferences[softwareDescription]]]]]"

result = imageManager.list_private_images(mask=object_mask)
pp(result)


```

### Calling API Directly

Get private image template

```python
import SoftLayer
from pprint import pprint as pp

# Declare the API client
client = SoftLayer.create_client_from_env(Y)

# declaring an object mask to get more information about the images templates
objectMask = """mask[summary, note, status[name],
storageRepository[datacenter],
transaction[transactionGroup,transactionStatus],
children[
    storageRepository[datacenter],
    blockDevices[diskImage[type]]
]]
"""


result = client.call(
    'Account',
    'getPrivateBlockDeviceTemplateGroups',
    mask=objectMask
)
pp(result)


```


### Important Manual Pages
- [ImageManager](https://softlayer-python.readthedocs.io/en/latest/api/managers/image/#SoftLayer.managers.image.ImageManager.list_private_images)
- [SoftLayer_Account::getPrivateBlockDeviceTemplateGroups()](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups)

## Update Locations

This will enable an Image Template in a selected datacenter. This is useful to do if you need to provision anything with this template, in the seleceted datacenter.


```python
"""
Update Locations

The script create(s) transaction(s) to set the archived block device available locations.

Important manual pages:
"""
import SoftLayer

from pprint import pprint as pp

# The virtual guest ID you want to create a template
imageTemplateId = 1796623

"""
Build a skeleton of SoftLayer_Location array containing the locations identifiers.
This locations can be obtained by using 
SoftLayer_Virtual_Guest_Block_Device_Template_Group::getStorageLocations method.
"""
locations = [
    {"id": 265592 },  # Amsterdam 1
    {"id": 1004997},  # Chennai 1
    {"id": 138124},   # Dallas 5 
]

# Declare a new API service object
client = SoftLayer.create_client_from_env()

try:
    # Creating the transaction to update locations on image template
    response = client.call(
            'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
            'setAvailableLocations', 
            locations,
            id=imageTemplateId
    )
    pp(response)
except SoftLayer.SoftLayerAPIError as e:
    """
    # Handle and Print any API errors
    """
    print("Unable to update the locations. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```


### Important Manual Pages

- [SoftLayer_Virtual_Guest_Block_Device_Template_Group::setAvailableLocations()](/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setAvailableLocations)
- [SoftLayer_Location](/reference/datatypes/SoftLayer_Location)
- [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group)


## Image from External Source

This script creates a transaction to import a disk image from an external source and creates a standard image template

Use [SoftLayer_Virtual_Guest::getCreateObjectOptions()](/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions/) for a list of `operatingSystemReferenceCode` options.

For IBM Cloud Object Storage, use [SoftLayer_Virtual_Guest_Block_Device_Template_Group::copyFromIcos()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyFromIcos/). 

```python
"""
Create Image Template from external source
"""
import SoftLayer
from pprint import pprint as pp

# Declare the group name to be applied to the imported template
name = 'imageTemplateTest'
# Declare the note to be applied to the imported template
note = 'An optional note'

'''
Declare referenceCode of the operating system software description for the imported VHD
Some Examples: 
CENTOS_6_32, CENTOS_6_64, CENTOS_7_64,
REDHAT_6_32, REDHAT_6_64, REDHAT_7_64,
UBUNTU_12_32, UBUNTU_12_64, UBUNTU_14_32, UBUNTU_14_64,
WIN_2003-STD-SP2-5_32, WIN_2003-STD-SP2-5_64,
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
client = SoftLayer.create_client_from_env()

try:
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group', 
        'createFromExternalSource',
        configuration
    )
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the image template from external source: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```

### Important manual pages:
- [SoftLayer_Virtual_Guest_Block_Device_Template_Group::createFromExternalSource()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource)
- [SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration](/reference/datatypes/SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration)
- [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group)


## Copy To External Source

This will take an existing Image Template, and copy it to an object storage repository.

For IBM Cloud Object Storage, use [SoftLayer_Virtual_Guest_Block_Device_Template_Group::copyToIcos()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToIcos/). 

```python
import SoftLayer

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
client = SoftLayer.create_client_from_env()
groupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

"""
Creating an SoftLayer_Container_Virtual_Guest_block_Device_Template_Configuration Skeleton
"""
configuration = {
    'uri': 'swift://' + objectStorageAccountName + '@' + clusterName + '/' + containerName + '/' + fileName
}

try:
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'copyToExternalSource',
        configuration,
        id=imageTemplateId
    )
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print('Unable to copy: \nfaultCode= %s, \nfaultString= %s'
          % (e.faultCode, e.faultString))
    exit(1)

```


### Important manual pages:
- [SoftLayer_Virtual_Guest_Block_Device_Template_Group::copyToExternalSource()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource)


## Delete Image Template

Removes an image template from your account by making an API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject)

```python
import SoftLayer

"""
The image template which you wish to delete
To get the list of images templates in your account 
call the SoftLayer_Account::getPrivateBlockDeviceTemplateGroups method
"""
imageTemplateId = 1796335

# Declare the API client
client = SoftLayer.create_client_from_env()
blockDeviceTemplateGroupService = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group']

try:
    # Calling the getObject to delete the image template
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'deleteObject',
        id=imageTemplateId
    )
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # Handle SoftLayer API Errors, if any..
    """
    print("Unable to delete the image template. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Important Manual Pages
- [SoftLayer_Account::getPrivateBlockDeviceTemplateGroups](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups)
- [SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject)

## Add/Remove BYOL OS License Attribute


This script will Add or Remove the BYOL attribute from an Image template. 

A template with the BYOL attribute will require you to provide a license after installation.
A template without the BYOL attribute will have a license provided by IBM, possibly at an additional cost.

```python
import SoftLayer
from pprint import pprint as pp

# The image template which you wish more details
imageTemplateId = 1797793

# Declaring the API client
client = SoftLayer.create_client_from_env()

try:
    # calling the deleteByolAttribute to remove OS License, this will return a boolean.

    ## REMOVE
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'deleteByolAttribute'
        id=imageTemplateId
    )

    ## ADD
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'addByolAttribute'
        id=imageTemplateId
    )

    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # Handle SoftLayer API errors
    """
    print("Unable to remove OS License (BYOL) on image template: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Important Manual Pages
- [Virtual_Guest_Block_Device_Template_Group::deleteByolAttribute()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteByolAttribute)
- [Virtual_Guest_Block_Device_Template_Group::addByolAttribute()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addByolAttribute)


## Disable/Enable CloudInit

Sets the Cloud Init Attribute for an Image Template

```python
import SoftLayer
from pprint import pprint as pp

# The image template which you wish more details
imageTemplateId = 1796623

# Declaring the API client
client = SoftLayer.create_client_from_env()
try:
    # calling the deleteCloudInitAttribute to disable cloudInit, this will return a boolean.

    # DISABLE
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'deleteCloudInitAttribute',
        id=imageTemplateId
    )
    # ENABLE
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'addCloudInitAttribute',
        id=imageTemplateId
    )
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to delete cloudInit on image template: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```

### Important Manual Pages
- [Virtual_Guest_Block_Device_Template_Group::deleteCloudInitAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteCloudInitAttribute)
- [Virtual_Guest_Block_Device_Template_Group::addCloudInitAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addCloudInitAttribute)


## Get Package and Items from Image

Will return a list of packages that this image template can be ordered on.

```python
import SoftLayer
from pprint import pprint as pp

# Declare the image template id
imageTemplateId = 429428

# Create a client instance
client = SoftLayer.Client()

# Build a SoftLayer_VIrtual_Guest_Block_Device_Template_Group object
imageTemplate = {"id": imageTemplateId}
try:
    packages = client.call(
        'SoftLayer_Product_Package',
        'getAvailablePackagesForImageTemplate',
        imageTemplate
    )
    print("============= PACKAGES ============")
    pp(packages)

    for package in packages:
        # If you already know the package you want to order from, you dont need to iterate through all possible packages.
        print("============= ITEMS for %s ============".format(package['id']))
        items = client.call(
            'SoftLayer_Product_Package',
            'getItemsFromImageTemplate',
            imageTemplate,
            id=package['id']
        )
        pp(items)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get available packages for an image faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```

A example with nicer output.

```python

# So we can talk to the SoftLayer API:
import SoftLayer
from prettytable import PrettyTable


# Declare the image template id
imageTemplateId = 33566
# Create a client instance
client = SoftLayer.Client()
# Build a SoftLayer_VIrtual_Guest_Block_Device_Template_Group object
imageTemplate = {"id": imageTemplateId}

# Declare an object mask to get prices for items
priceMask = 'mask[pricingLocationGroup[locations]]'


# Get available packages for the image template
packages = client.call(
    'SoftLayer_Product_Package',
    'getAvailablePackagesForImageTemplate',
    imageTemplate
)
for package in packages:
    # Build table
    x = PrettyTable(["Price Id", "Item Id", "Description", "Datacenters"])
    x.align["Price Id"] = "l"  # Left align city names
    x.padding_width = 1
    print('***** Package: %s *****' % package['id'])
    # Get Item Prices, in order to verify the active prices
    itemPrices = client['SoftLayer_Product_Package'].getItemPrices(id=package['id'], mask=priceMask)
    # Get Items from the image template
    items = client['SoftLayer_Product_Package'].getItemsFromImageTemplate(imageTemplate, id=package['id'])
    # We define a item verification, in order to avoid duplicate data in the loop
    itemVerication = 0
    for item in items:
        if item['id'] != itemVerication:
            for itemPrice in itemPrices:
                if itemPrice['item']['id'] == item['id']:
                    locationDC = ''
                    pack = ''
                    if 'pricingLocationGroup' in itemPrice:
                        for locations in itemPrice['pricingLocationGroup']['locations']:
                            locationDC = locationDC + ' ' + locations['longName']
                    else:
                        locationDC = 'Standard price'
                    x.add_row([itemPrice['id'], itemPrice['item']['id'], itemPrice['item']['description'], locationDC])
            itemVerication = item['id']
    print(x)


```

### Important manual pages:
- [SoftLayer_Product_Package::getAvailablePackagesForImageTemplate()](/reference/services/SoftLayer_Product_Package/getAvailablePackagesForImageTemplate)
- [SoftLayer_Product_Package::getItemsFromImageTemplate()](/reference/services/SoftLayer_Product_Package/getItemsFromImageTemplate)



## Share/Unshare Template

The script shares an image template to another account.

```python

import SoftLayer
from pprint import pprint as pp

# The image template which you wish to share
imageTemplateId = 1796623

# the account you wish to share the image template
accountToShare = 207819

# Declare the API client
client = SoftLayer.create_client_from_env()
try:
    # Calling the permitSharingAccess method to share the image template

    # PERMIT
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'permitSharingAccess',
        accountToShare, id=imageTemplateId
        )

    # DENY
    result = client.call(
        'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        'denySharingAccess',
        accountToShare, id=imageTemplateId
        )
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to share the image template. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
