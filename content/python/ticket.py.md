---
title: "Working with Tickets"
description: "A few examples on interacting with Tickets"
date: "2020-07-03"
classes: 
    - "SoftLayer_Ticket"
    - "SoftLayer_Ticket_Subject"
    - "SoftLayer_Brand"
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "tickets"
    - "brands"
---

## Getting ticket Subjects

Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the 
[SoftLayer_Ticket_Subject](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject) service. 
The following example will output all of the Ticket Subjects:

```python

import SoftLayer
client = SoftLayer.Client()
def getSubjects(self):
    mask = "mask[group]"
    subjects = client.call('SoftLayer_Ticket_Subject', 'getAllObjects', mask=mask)
    print("|Subject Id | Subject Name | Group Name |")
    print("| --- | --- | --- |")
    for subject in subjects:
        print("|%s| %s| %s|" % (subject['id'], subject['name'], subject['group']['name']))

```

### Subjects
|Subject Id | Subject Name | Group Name |
| --- | --- | --- |
|1522| API Question| Support|
|1001| Accounting Request| Accounting|
|1181| CDN Question| SysAdmin|
|1261| Colocation Service Request| Hardware|
|1041| DNS Request| Support|
|1201| DOS/Abuse Issue| Support|
|1121| Hardware Firewall Question| Support|
|1021| Hardware Issue| Support|
|1122| Hardware Load Balancer Question| Support|
|1081| Licensing Question| Support|
|1141| Mail Server Issue| Support|
|1004| OS Reload Question| Support|
|1005| Portal Information Question| Support|
|1061| Private Network Question| Support|
|1022| Public Network Question| Support|
|1003| Reboots and Console Access| Support|
|1002| Sales Request| Sales|
|1603| Sales Request - Compute & Infrastructure| Sales|
|1645| Sales Request - Firewall Service| Sales|
|1647| Sales Request - General Question| Sales|
|1605| Sales Request - Network & Security Services| Sales|
|1643| Sales Request - Other Services| Sales|
|1607| Sales Request - Upgrades & Add-ons| Sales|
|1101| Security Issue| Support|
|1161| Storage Question| Support|
|1221| Transcoding Question| Support|
|1723| VMware Solutions| VMware Solutions|
|1482| Vyatta Question| SysAdmin|


### Create Standard Ticket
Create a standard support ticket. Use a standard support ticket if you need to work out a problem related to 
SoftLayer's hardware, network, or services.

```python
import SoftLayer
client = SoftLayer.Client()
def createTicket(self):
    current_user = client.call('SoftLayer_Account', 'getCurrentUser')
    body = "I'm testing API ticket creation. Please close this ticket if you see it. Thanks."
    serverId = 1317535
    serverPass = '12345'
    # http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
    new_ticket = {
        'subjectId': 1021,
        'assignedUserId': current_user['id'],
        'title': 'TESTING TICKET 003',
        'priority': 4
    }
    # parameter list is from, need to be in order http://sldn.softlayer.com/reference/services/softlayer_ticket/createStandardTicket
    created_ticket = client.call('SoftLayer_Ticket', 'createStandardTicket', 
        new_ticket, body, serverId, serverPass, None, None, None, 'HARDWARE')
    pp(created_ticket)
```

###Create Ticket Attached File

```python
import SoftLayer
# client configuration
ENDPOINT = "http://api.softlayer.com/v3/sldn/xmlrpc/"
# Your SoftLayer API username.
USERNAME = ''
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
API_KEY = 'apikey_goes_here'

# Declare the API client
client = SoftLayer.Client(endpoint_url=ENDPOINT, username=USERNAME,api_key=API_KEY)
#client = SoftLayer.Client(username=USERNAME,api_key=API_KEY)

templateObject = {
                    "assignedUserId" : 104672,
                    "notifyUserOnUpdateFlag" : True,
                    "subjectId" : 1522,
                    "title" : "ticket example"
                   }

contents = 'this the ticket contet'

attachedFiles = [
                  {
                    "data" : "gICBdDQp9",
                    "filename" : "test2.txt"
                  }  
                ]

attachID = 0
rootPassword = ""
controlPanelPassword = ""
accesPort = "" 
attachedFiles = attachedFiles

try:
    # getting the VLANs
    result = client['SoftLayer_Ticket'].createStandardTicket(templateObject, contents, attachID, rootPassword ,  controlPanelPassword , accesPort , attachedFiles)
    print (result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.            
    print("Unable to get Vlans. "
          % (e.faultCode, e.faultString))

```

###Create Ticket Attached File Encode

```python
import SoftLayer
import base64
# client configuration
ENDPOINT = "http://api.softlayer.com/v3/sldn/xmlrpc/"
# Your SoftLayer API username.
USERNAME = ''
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
API_KEY = 'apikey_goes_here'

# Declare the API client
#client = SoftLayer.Client(endpoint_url=ENDPOINT, username=USERNAME,api_key=API_KEY)
client = SoftLayer.Client(username=USERNAME,api_key=API_KEY)

encoded_string = ""

with open("C:\\test.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

templateObject = {
                    "assignedUserId" : 205832,
                    "notifyUserOnUpdateFlag" : True,
                    "subjectId" : 1522,
                    "title" : "Test Ticket Please Close at your earliest convenience"
                   }

contents = 'this the ticket contet'

attachedFiles = [
                  {
                    "data" : encoded_string,
                    "filename" : "test2.png"
                  }  
                ]

attachID = 0
rootPassword = ""
controlPanelPassword = ""
accesPort = "" 

try:
    # getting the VLANs
    result = client['SoftLayer_Ticket'].createStandardTicket(templateObject, contents, attachID, rootPassword ,  controlPanelPassword , accesPort , attachedFiles)
    print (result)
except SoftLayer.SoftLayerAPIError as e:
    # If there was an error returned from the SoftLayer API then bomb out with the
    # error message.            
    print("Unable to get Vlans. "
          % (e.faultCode, e.faultString))

```

###Create Standard Ticket getting Subject and Users

```python

import SoftLayer.API

USERNAME = 'set me'
API_KEY = 'set me'

# The name of the user to assign the ticket
assingToUser = "pulse-lab"

# The subject name of the ticket
subjectName = "Vyatta Question"

# Creating the services
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']
ticketSubjectService = client['SoftLayer_Ticket_Subject']
ticketService = client['SoftLayer_Ticket']

try:
    # We are setting a filter to get the users which status is active
    objectFilterUsers = {
        'users': {
            'userStatus': {
                'keyName': {
                    'operation': 'ACTIVE'
                }
            }
        }
    }

    # Getting all the active users in the account.
    users = accountService.getUsers(filter=objectFilterUsers)
    # Getting all available subjects for the ticket
    subjects = ticketSubjectService.getAllObjects()

    # Looking for the correct assingToUserId
    assingToUserId = 0
    for user in users:
        if user['username'] == assingToUser:
            assingToUserId = user['id']

    # Looking for the correct subjectId
    subjectId = 0
    for subject in subjects:
        if subject['name'] == subjectName:
            subjectId = subject['id']

    # Creating the skeleton for the SoftLayer_Ticket template
    templateObject = {
        "assignedUserId": assingToUserId,
        "notifyUserOnUpdateFlag": True,
        "subjectId": subjectId,
        "title": "the title for the ticket"
    }

    # The contents for the ticket
    content = "this is the content"

    # Creating the new ticket
    result = ticketService.createStandardTicket(templateObject, content)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create standard ticket faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```

###List Tickets

The script retrieves all the tickets in a brand account.
It displays the same result like in https://agent.softlayer.com/support/ticket/list.

```python
import json

import SoftLayer.API

USERNAME = 'set me'
API_KEY = 'set me'

brandId = 4

client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY, timeout=500)
brandService = client['SoftLayer_Brand']

objectMask = "mask[group[name], status[name], statusId, id, createDate, title, assignedUser[username], " \
             "attachedFileCount, totalUpdateCount, modifyDate, lastEditType, newUpdatesFlag, attachedHardwareCount, " \
             "attachedVirtualGuestCount, priority, account[companyName, accountStatus[name]]," \
             " assignedAgents[username], state[stateType], scheduledActions[transactionGroup, " \
             "ticketScheduledActionReference] ]"
objectFilter = {
    "tickets": {"status": {"name": {"operation": "in", "options": [{"name": "data", "value": ["Open", "Assigned"]}]}}}}

try:
    result = brandService.getTickets(id=brandId, filter=objectFilter, mask=objectMask)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the tickets. "
          % (e.faultCode, e.faultString))

```
