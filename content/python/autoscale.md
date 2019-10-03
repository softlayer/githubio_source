---
title: "Autoscale"
description: "Working with the SoftLayer_Scale_Group service."
date: "2019-10-03"
classes: 
    - "SoftLayer_Scale_Group"
    - "SoftLayer_Scale_Policy"
    - "SoftLayer_Scale_Member"
tags:
    - "scalegroups"
---

[Autoscale UI](https://cloud.ibm.com/classic/autoscale/)
[Autoscale CLU](https://softlayer-python.readthedocs.io/en/latest/cli/autoscale.html)
[Autoscale Docs](https://cloud.ibm.com/docs/vsi?topic=virtual-servers-about-auto-scale)


```python
import SoftLayer
from pprint import pprint as pp

class autoscale():

    def __init__(self):

        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger


    def list(self):
        """List out autoscale groups"""
        mask = "mask[status,virtualGuestMemberCount]"
        groups = self.client.call('SoftLayer_Account', 'getScaleGroups', mask=mask, iter=True)
        print("Id, Name, Guests")
        for group in groups:
            print("{}, {}, {}".format(group['id'], group['name'], group['virtualGuestMemberCount']))

    def get_group_template(self, group_id):
        mask = "mask[virtualGuestMemberTemplate]"
        group = self.client.call('SoftLayer_Scale_Group', 'getObject', mask=mask, id=group_id)
        pp(group['virtualGuestMemberTemplate'])


    def set_group_name(self, group_id, new_name=""):
        """Sets the name of an autoscale group

        Editing some of the other properties in https://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group/
        can be done the same way.
        """
        template = {}
        template['name'] = new_name

        group = self.client.call('SoftLayer_Scale_Group', 'editObject', template, id=group_id)
        
    def toggle_scale_group(self, group_id, suspended=False):
        """Suspend or un-suspend a group

        suspend=False to turn the group ON
        suspend=True to turn the group OFF
        """
        template = {
            "id": scaleGroupId,
            "suspendedFlag": suspended
        }
        group = self.client.call('SoftLayer_Scale_Group', 'editObject', template, id=group_id)

    def create_scale_group(self):
        """Create a scale group
        
        https://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group/ for the template options.
        """
        template = {
            "cooldown" : 1800,
            "maximumMemberCount" : 5,
            "minimumMemberCount" : 1,
            "name" : "testRaul2cb03",
            "regionalGroupId" : 102,
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
                        "diskImage" : {"capacity" : 25}
                    },  # Device 1 is usually swap, which is why we skip to device 2
                        {
                            "device" : 2,
                            "diskImage" : { "capacity" : 10}
                        }
                    ],
                    "datacenter" : {"name" : "dal13"},
                    "hourlyBillingFlag" : True,
                    "localDiskFlag" : False,
                    "networkComponents" : [{ "maxSpeed" : 100}],
                    "operatingSystemReferenceCode" : "CENTOS_LATEST",
                    "privateNetworkOnlyFlag" : False#,
         #           "sshKeys" : [{"id" : 246}]    
                },
                "virtualGuestMemberCount" : 0,
         #       "networkVlans" : [
         #           {"networkVlanId" : 542438},
         #           {"networkVlanId" : 542436}
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
        group = self.client.call('SoftLayer_Scale_Group', 'createObject', template)
        pp(group)
        return group

    def delete_group(self, group_id):
        """Remove a scale group
        
        use https://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/forceDeleteObject to also remove any existing guests. 
        """
        self.client.call('SoftLayer_Scale_Group', 'deleteObject', id=group_id)

    def scale_group(self, group_id, amount=0):
        """Scale a group by amount
        
        if amount if negative, group will scale down by that amount.
        """
        result = self.client.call('SoftLayer_Scale_Group', 'scale', amount, id=group_id)

    def get_logs(self, group_id):
        result = self.client.call('SoftLayer_Scale_Group', 'getLogs', id=group_id)
        pp(result)

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

if __name__ == "__main__":
    main = autoscale()
    main.list()
    
    # main.set_group_name(2255094, new_name="ajcb-autoscale12")
    # main.get_group_template(2255094)
    # main.debug()

```