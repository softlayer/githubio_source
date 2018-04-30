---
title: "add_locations_to_image_template.py"
description: "add_locations_to_image_template.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Location"
tags:
    - "images-templates"
---


```
"""
Update Locations

The script create(s) transaction(s) to set the archived block device available locations.

Important manual pages:
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setAvailableLocations
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Location
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# The virtual guest ID you want to create a template
imageTemplateId = 1796623
# The name of the image template

"""
Build a skeleton of SoftLayer_Location array containing the locations´ identifiers.
This locations can be obtained by using 
SoftLayer_Virtual_Guest_Block_Device_Template_Group::getStorageLocations method.
"""
locations = [
    {
        "id": 265592, # Amsterdam 1
    },
    {
        "id": 1004997, # Chennai 1
    },
    {
        "id": 138124, # Dallas 5
    },
    {
        "id": 449494, # Dallas 9
    },
    {
        "id": 1441195, # Dallas 10
    }
]

# Declare a new API service object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)

try:
    # Creating the transaction to update locations on image template
    response = client['SoftLayer_Virtual_Guest_Block_Device_Template_Group'].setAvailableLocations(locations, id=imageTemplateId)
    pp(response)
except SoftLayer.SoftLayerAPIError as e:
    """
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.
    """
    print("Unable to update the locations. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
