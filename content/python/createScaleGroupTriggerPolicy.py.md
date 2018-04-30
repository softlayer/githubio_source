---
title: "createScaleGroupTriggerPolicy.py"
description: "createScaleGroupTriggerPolicy.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Scale_Policy_Trigger_OneTime"
    - "SoftLayer_Scale_Policy_Trigger_Repeating"
    - "SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch"
    - "SoftLayer_Scale_Group"
    - "SoftLayer_Scale_Policy_Trigger_ResourceUse"
tags:
    - "scalegroups"
---


```
# Example to create a scale group with a policy and a trigger
# trigger will be: If my CPU Percentage is greater than 80 for 30 Minute(s)
# Action: Scale group to 1 Member (absolute)
# reference pages
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Policy_Trigger_ResourceUse
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group
# http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group
# http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/createObject
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
                "maximumMemberCount" : 2,
                "minimumMemberCount" : 1,
                "name" : "testRaul2cb04",
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
                "virtualGuestMemberCount" : 0,
         #       "networkVlans" : [
         #           {
         #               "networkVlanId" : 542438
         #           },
         #           {
         #               "networkVlanId" : 542436
         #           }
         #       ]
                "policies" : [
                    {
                       "name" : "myPolicy",
                       "cooldown" : 120,
                       # creating the triggers you can define the following triggers:
                       # oneTimeTriggers http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Policy_Trigger_OneTime
                       # repeatingTrigger http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Policy_Trigger_Repeating
                       # resourceUseTrigger http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Policy_Trigger_ResourceUse
                       "resourceUseTriggers" : [
                            {
                                "complexType": "SoftLayer_Scale_Policy_Trigger_ResourceUse",
                                "deleteFlag": False,
                                "watches" : [
                                    {
                                        "algorithm" : "EWMA",
                                        "deleteFlag": False,
                                        "metric" : "host.cpu.percent",
                                        "operator" : ">",
                                        "period" : 1800,
                                        "value" : 80,
                                        "complexType": "SoftLayer_Scale_Policy_Trigger_ResourceUse_Watch"
                                    }
                                ]
                            }
                       ],
                        "scaleActions" : [
                            {
                                "amount" : 1,
                                "scaleType" : "ABSOLUTE"
                            }
                        ]
                    }
                ]
         
}

result = scaleGroupService.createObject(template)
print (result)
```
