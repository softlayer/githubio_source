---
title: "createTicketAttachedFileEnconde.rb"
description: "createTicketAttachedFileEnconde.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```
#!/usr/bin/env ruby

require 'softlayer_api'
require 'pp'
require 'base64'

# Your SoftLayer API key.
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
username = ''
key = 'apikey_goes_here'

path = "C:\\Automatio competences.xlsx"
path = "C:\\test.png"
name = "framework.xlsx"
name = "test.png"

contents = 'Test Ticket Please Close at your earliest convenience'

file = File.open(path,'rb') { |io| io.read }
encode = Base64.encode64(file)


attachedFiles = [
{
'data' => encode,
#'data' => File.open("C:\\Automatio competences.xlsx", "rb").read,
'filename' => name
} 
]


template = {
'subjectId' => 1522,
'contents' => contents,
'assignedUserId' => 205832,
'title' => "Test Ticket Please Close at your earliest convenience"
}

# Declare the API client
client = SoftLayer::Client.new( :username => username,:api_key => key)
ticket_service = client['SoftLayer_Ticket']

new_ticket = ticket_service.createStandardTicket(template, contents, 0, '', '', '', attachedFiles)
print (new_ticket)
```
