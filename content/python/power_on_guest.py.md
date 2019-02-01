---
title: "Change power settings on a VSI"
description: "PowerOn, PowerOFf"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Acount"
tags:
    - "virtualserver"
---


```
"""
Power off Guest

The scripts will look for a VSI which has an specific
hostname and the it powers on the VSI by making a single call
to the SoftLayer_Virtual_Guest::powerOn method.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Acount/
http://sldn.softlayer.com/reference/services/SoftLayer_Acount/getVirtualGuests
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/powerOn

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# The name of the machine you wish to power off
virtualGuestName = 'vsiHostname'

# Declare a new API service object
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)


try:
    # Getting all virtual guest that the account has:
    virtualGuests = client['SoftLayer_Account'].getVirtualGuests()
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to retrieve virtual guest. "
          % (e.faultCode, e.faultString))

# Looking for the virtual guest
virtualGuestId = ''
for virtualGuest in virtualGuests:
    if virtualGuest['hostname'] == virtualGuestName:
        virtualGuestId = virtualGuest['id']

try:
    # Power off the virtual guest
    virtualMachines = client['SoftLayer_Virtual_Guest'].powerOn(id=virtualGuestId)
    print ("powered ON")

    # PowerOFF
    # virtualMachines = client['SoftLayer_Virtual_Guest'].powerOff(id=virtualGuestId)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to power on the virtual guest"
          % (e.faultCode, e.faultString))

```
