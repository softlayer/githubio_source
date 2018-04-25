---
title: "update_firmware.py"
description: "update_firmware.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Update the firmware in a BareMetal server

The script makes a single call to SoftLayer_Hardware_Server::createFirmwareUpdateTransaction
method to update the firmware in a bare metal server. It will bring your server offline for
approximately 20 minutes while the updates are in progress.

See below for more details

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/createFirmwareUpdateTransaction

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

# Declare the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareServerService = client['SoftLayer_Hardware_Server']

# The if of the bare metal server you wish to update the firmware
hardwareId = 284776

"""
The firmware to update
set the values with "1" to update and "0" skip
"""
ipmi = 1
raidController = 1
bios = 1
hardDrive = 0

try:
    result = hardwareServerService.createFirmwareUpdateTransaction(ipmi, raidController, bios, hardDrive, id=hardwareId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to update the firmware: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))
    exit(1)

```
