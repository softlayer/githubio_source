---
title: "edit_server.py"
description: "edit_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Edit a bare metal server's basic information

Change the notes property for a single bare metal server record to the sentence "This
is my fastest server!" using the editObject() method in the
SoftLayer_Hardware_Server API service. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/editObject
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# The (host) name of the server we wish to edit.
serverName = 'testServer'

"""
Define the new local properties to set.

A SoftLayer_Hardware_Server record has a few local properties that you can
change via the API. Every service's editObject() method takes a single
parameter, a skeleton object that only defines the properties we wish to
change. While we're only editing a server's notes in this example you can
also use editObject() to edit the server's host name and domain record.
"""
editTemplate = {
    'notes': 'This is my fastest server!'
}

# The id of the bare metal you wish to edit
hardwareId = 284776

# Declare a new API service object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)


"""
Call the getHardware() method from the SoftLayer_Account API service to get
a list of hardware on your account, including id numbers.
"""
try:
    hardwareList = client['SoftLayer_Account'].getHardware()
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to retrieve bare metal list: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

# Looking for the server name to get its id
for hardware in hardwareList:
    if hardware['hostname'] == serverName:
        hardwareId = hardware['id']

# If the server name was not found we throw an error message.
if hardwareId == '':
    raise Exception("Unable to find the server with the name " + serverName)

try:
    # Edit our server record.
    result = client['SoftLayer_Hardware_Server'].editObject(editTemplate, id=hardwareId)
    print('Bare Metal Server edited')
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to edit the bare metal server: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
