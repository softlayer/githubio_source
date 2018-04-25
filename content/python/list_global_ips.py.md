---
title: "list_global_ips.py"
description: "list_global_ips.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet_IpAddress_Global"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Subnet_IpAddress"
tags:
    - "globalips"
---


```
"""
List global IP address

Example to list the global IP address from an account
and see if a specific IP is assigned to a specific host

Important manual pages:
http://sldn.softlayer.com/article/python
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getGlobalIpRecords
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The global Ip address you want to verify if it is assigned
globalIpId = 11222

# The hostname of the virtual guest that you want to verify if it is assigned
hostnameAssigned = "danone-fw1"

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# Declaring a mask to get more details for the global IP adreesess
objectMask = "mask[destinationIpAddress[hardware, virtualGuest]]"

try:
    # Getting the global IP list for the account
    globalIps = accountService.getGlobalIpRecords(mask=objectMask)
except SoftLayer.SoftLayerAPIError as e:
    # In case there was an error, we print the following
    print("Unable to retrieve the global IP address faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)


globalIpFound = False
for globalIp in globalIps:
    if globalIpId == globalIp['id']:
        globalIpFound = True
        targetIp = globalIp['destinationIpAddress']['ipAddress']
        associatedHostname = ""
        if 'hardware' in globalIp['destinationIpAddress'].keys():
            associatedHostname = globalIp['destinationIpAddress']['hardware']['hostname']
        elif 'virtualGuest' in globalIp['destinationIpAddress'].keys():
            associatedHostname = globalIp['destinationIpAddress']['virtualGuest']['hostname']
        if associatedHostname == hostnameAssigned:
            print("the global IP is assigned.")
        else:
            print("the global IP is not assigned.")

if not globalIpFound:
    print("The global IP address does not exist.")

```
