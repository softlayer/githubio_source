---
title: "backup_netscaler.py"
description: "backup_netscaler.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller"
    - "SoftLayer_Account"
tags:
    - "netscalers"
---


```
"""
NetScalers Backups

Example to take Netscalers backups, the script will list all the Netscalers in the account
and will look for an specific Netscaler in order to take a backup

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller/saveCurrentConfiguration
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller
https://sldn.softlayer.com/reference/services/SoftLayer_Account/getApplicationDeliveryControllers
https://sldn.softlayer.com/reference/services/SoftLayer_Account/
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The name of the netscaler you wish take the backup
netscalerName = "SLADC208473-1"

# Declare the API client and creating the services that we need
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']
networkApplicationDeliveryControllerService = client['SoftLayer_Network_Application_Delivery_Controller']


try:
    # Getting all the netscalers devices in our account
    netscalers = accountService.getApplicationDeliveryControllers()
    # Looking for the nextsaler we whish to take the backup
    for netscaler in netscalers:
        if netscaler['name'] == netscalerName:
            # Taking the back up in our netscaler
            result = networkApplicationDeliveryControllerService.saveCurrentConfiguration("This is the note for my backup", id=netscaler['id'])
            print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to backup the Netscaler faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
