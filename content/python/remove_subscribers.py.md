---
title: "remove_subscribers.py"
description: "remove_subscribers.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_User_Customer"
tags:
    - "suscribers"
---


```
"""
Remove subscribers

The scripts remove subscribers from an arbitrary VSI machine.
for more information see below:

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMonitoringAgents
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/removeActiveAlarmSubscriber
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/SoftLayer_User_Customer/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent/SoftLayer_User_Customer

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# Client configuration
USERNAME = 'set me'
API_KEY = 'set me'

hostnames = ["rctest", "rctest2"]
mailsToRemove = ["Nelson.Cabero@jalasoft.com"]

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    # Getting all virtual servers on the account
    vServers = client['Account'].getVirtualGuests()

    for hostname in hostnames:
        for vServer in vServers:
            if hostname == vServer['hostname']:
                vSertverId = vServer['id']
                # Getting all the agents in the virtual machine
                agents = client['Virtual_Guest'].getMonitoringAgents(id=vSertverId)
                for agent in agents:
                    agentId = agent['id']
                    agentName = agent['name']
                    elegibleSubscribers = client['SoftLayer_Monitoring_Agent'].getEligibleAlarmSubscibers(id=agentId)
                    for mailToRemove in mailsToRemove:
                        for elegibleSubscriber in elegibleSubscribers:
                            if 'id' in elegibleSubscriber:
                                suscriberId = elegibleSubscriber['id']
                                userData = client['SoftLayer_User_Customer'].getObject(id=suscriberId)
                                if mailToRemove.strip() == userData['email'].strip():
                                    removed = client['SoftLayer_Monitoring_Agent'].removeActiveAlarmSubscriber(suscriberId, id=agentId)
                                    if removed:
                                        print(str(suscriberId) + "For hostname: " + hostname + " with ID " + str(vSertverId) + " in the agent for " + agentName + str(agentId) + " the mail " + mailToRemove + " has been removed.")
                                    else:
                                        print("ERROR - For hostname: " + hostname + " with ID " + str(vSertverId) + " in the agent for " + agentName + " the mail " + mailToRemove + " has not been removed.")

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to remove subscriber faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
