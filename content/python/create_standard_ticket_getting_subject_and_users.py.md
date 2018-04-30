---
title: "create_standard_ticket_getting_subject_and_users.py"
description: "create_standard_ticket_getting_subject_and_users.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Ticket"
    - "SoftLayer_Ticket_Subject"
tags:
    - "users"
---


```
"""
Create standard ticket

The script creates a standard ticket, it makes a single call
to the SoftLayer_Ticket::createStandardTicket method
For more information see:

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject/getAllObjects
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createStandardTicket

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
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
