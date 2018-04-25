---
title: "createScaleGroup.py"
description: "createScaleGroup.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
#!/usr/bin/env python3

import SoftLayer
# client configuration
# Your SoftLayer API username.
USERNAME = ''
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
API_KEY = 'apikey_goes_here'

# Declare the API client
client = SoftLayer.Client(username=USERNAME,api_key=API_KEY)
scaleGroupService = client['SoftLayer_Scale_Group']
template = {
                "cooldown" : 1800,
                "maximumMemberCount" : 5,
                "minimumMemberCount" : 1,
                "name" : "testRaul2cb03",
                "regionalGroupId" : 102,
                "suspendedFlag" : False,
                "terminationPolicyId" : 2,
                "virtualGuestMemberTemplate" : {
                    "domain" : "test.com",
                    "hostname" : "hostnametest",
                    "maxMemory" : 1024,
                    "postInstallScriptUri" : "https://www.softlayer.com",
                    "startCpus" : 1,
                    "userData" : [{
                        "value" : "the userData"
                    }],
                    "blockDevices" : [
                        {
                            "device" : 0,
                            "diskImage" : {
                                "capacity" : 25
                            }
                        },
                        
                        {
                            "device" : 2,
                            "diskImage" : {
                                "capacity" : 10
                            }
                        }
                    ],
                    "datacenter" : {
                        "name" : "hkg02"
                    },
                    "hourlyBillingFlag" : True,
                    "localDiskFlag" : False,
                    "networkComponents" : [
                        {
                            "maxSpeed" : 10
                        }
                    ],
                    "operatingSystemReferenceCode" : "CENTOS_LATEST",
                    "privateNetworkOnlyFlag" : False#,
         #           "sshKeys" : [
         #               {
         #                   "id" : 246
         #               }
         #           ]    
                },
                "virtualGuestMemberCount" : 0#,
         #       "networkVlans" : [
         #           {
         #               "networkVlanId" : 542438
         #           },
         #           {
         #               "networkVlanId" : 542436
         #           }
         #       ]
}

result = scaleGroupService.createObject(template)
print(result)

```
