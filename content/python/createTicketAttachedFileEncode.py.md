---
title: "createTicketAttachedFileEncode.py"
description: "createTicketAttachedFileEncode.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Ticket"
tags:
    - "tickets"
---


```
import SoftLayer
import base64
# client configuration
ENDPOINT = "http://stable.application.qadal0501.softlayer.local/v3/sldn/xmlrpc/"
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
