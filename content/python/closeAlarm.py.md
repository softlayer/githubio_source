---
title: "closeAlarm.py"
description: "closeAlarm.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "alarm"
---


```
# example to delete an specific alarm from a virtual server
#
# some reference pages
#
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMonitoringActiveAlarms
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/closeAlarm
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
import SoftLayer

# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal:
# https://manage.softlayer.com/Administrative/apiKeychain

# The id of the virtual server which contains the alarm you wish to delete
# you can get the virtual guest ID by calling the SoftLayer_Account::getVirtualGuests method
# for more reference see: http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
# eg.
# client = SoftLayer.Client(username=username,api_key=key)
# accountService = client['SoftLayer_Account']
# virtualServers = accountService.getVirtualGuests();
# print (virtualServers)
virtualServerID = 4979090

# The start date and end date that you want to search an specific alarm
startDate = "2000-01-01"
endDate = "2014-08-28"
# The alarm's message you wish to delete
messageAlarm = "BootAlarm: Computer has been rebooted at 2014.7.3 14:31:39"

# Declare a new API service object
client = SoftLayer.Client()
virtualGuestService = client['SoftLayer_Virtual_Guest']

# Getting all the active alarms in the Virtual Server
activeAlarms = virtualGuestService.getMonitoringActiveAlarms(startDate, endDate, id = virtualServerID)
# Looking for the alarm which contains the specific message
for alarm in activeAlarms:
    if alarm['message'] == messageAlarm:
        # deleting the alarm
        result = virtualGuestService.closeAlarm(alarm['alarmId'],id = virtualServerID)
        print (result)
 
```
