---
title: "list_passwords.py"
description: "list_passwords.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
    - "SoftLayer_Hardware_Server"
tags:
    - "managepassword"
---


```
"""
List the passwords of the devices in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Search
http://sldn.softlayer.com/reference/services/SoftLayer_Search/advancedSearch

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
searchService = client['SoftLayer_Search']

objectMask = "mask[resource(SoftLayer_Hardware)[softwareComponents.passwords,softwareComponents.softwareLicense.softwareDescription.name,softwareComponents.softwareLicense.softwareDescription.operatingSystem,softwareComponents.softwareLicense.softwareDescription.manufacturer,softwareComponents.passwords.id,fullyQualifiedDomainName,id,serviceProviderId,primaryIpAddress,softwareComponents.passwords.password,softwareComponents.passwords.username,softwareComponents.passwords.createDate,softwareComponents.passwords.modifyDate,softwareComponents.passwords.notes,softwareComponents.passwords.port,softwareComponents.softwareLicense.softwareDescription.version,datacenter.longName,datacenter.id],resource(SoftLayer_Hardware_Server)[softwareComponents.passwords,softwareComponents.softwareLicense.softwareDescription.name,softwareComponents.softwareLicense.softwareDescription.operatingSystem,softwareComponents.softwareLicense.softwareDescription.manufacturer,softwareComponents.passwords.id,fullyQualifiedDomainName,id,serviceProviderId,primaryIpAddress,softwareComponents.passwords.password,softwareComponents.passwords.username,softwareComponents.passwords.createDate,softwareComponents.passwords.modifyDate,softwareComponents.passwords.notes,softwareComponents.passwords.port,softwareComponents.softwareLicense.softwareDescription.version,datacenter.longName,datacenter.id],resource(SoftLayer_Virtual_Guest)[softwareComponents.passwords,softwareComponents.softwareLicense.softwareDescription.name,softwareComponents.softwareLicense.softwareDescription.operatingSystem,operatingSystem.softwareLicense.softwareDescription.manufacturer,operatingSystem.softwareLicense.softwareDescription.name,softwareComponents.passwords.id,fullyQualifiedDomainName,id,primaryIpAddress,softwareComponents.passwords.password,softwareComponents.passwords.username,softwareComponents.passwords.createDate,softwareComponents.passwords.modifyDate,softwareComponents.passwords.notes,softwareComponents.passwords.port,operatingSystem.softwareLicense.softwareDescription.operatingSystem,datacenter.longName,datacenter.id]]"

try:
    devices = searchService.advancedSearch("_objectType:SoftLayer_Hardware,SoftLayer_Virtual_Guest", mask=objectMask)
    passwords = []
    for device in devices:
        if 'resource' in device:
            for component in device['resource']['softwareComponents']:
                for pas in component['passwords']:
                    password = {}
                    password['name'] = device['resource']['fullyQualifiedDomainName']
                    password['username'] = pas['username']
                    password['password'] = pas['password']
                    password['softwareComponentId'] = component['id']
                    password['passwordId'] = pas['id']
                    password['deviceId'] = device['resource']['id']
                    passwords.append(password)

    print(json.dumps(passwords, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the passwords faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
