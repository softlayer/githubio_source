---
title: "create_cancel_server_ticket.py"
description: "create_cancel_server_ticket.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Ticket"
tags:
    - "cancelservers"
---


```
"""
Create cancel server ticket

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/
http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createCancelServerTicket

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username.
USERNAME = 'set me'
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain.
API_KEY = 'set me'

# Declare the API client and creating the services that we need
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
ticketService = client['SoftLayer_Ticket']

serverId = 198982
reason = "No longer needed"
content = "cancel because we want a new server"

try:
    result = ticketService.createCancelServerTicket(serverId, reason, content)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create ticket faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
