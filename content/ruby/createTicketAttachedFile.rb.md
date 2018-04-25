---
title: "createTicketAttachedFile.rb"
description: "createTicketAttachedFile.rb"
date: "2018-04-25"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Ticket"
tags:
    - "ticket"
---


```
require 'softlayer_api'

user = ""

api_key  = "apikey_goes_here"

endpoint_url = "http://stable.application.qadal0501.softlayer.local/v3/sldn/xmlrpc/"


# Declare the API client to use the SoftLayer_Product_Package API service
client = SoftLayer::Client.new(:username => user,:api_key => api_key, :endpoint_url =>endpoint_url )

ticketService = client.service_named("SoftLayer_Ticket")

templateObject = {
                    'assignedUserId' => 104672,
                    'notifyUserOnUpdateFlag' => true,
                    'subjectId' => 1522,
                    'title' => 'ticket example'
                   }

contents = 'this the ticket contet'

attachedFiles = [
                  {
                    'data' => 'aHR0cHM6Ly88VXNlcm5hbWU+OjxBUGlLZXk+apikey_goes_hereapikey_goes_hereapikey_goes_hereapikey_goes_hereapikey_goes_hereCiAgICBdDQp9',
                    'filename' => "test2.txt"
                  }  
                ]

begin
  # creates the notification
  result = ticketService.createStandardTicket(templateObject=templateObject, contents, attachID = 0, rootPassword = '',  controlPanelPassword ='', accesPort = '' , attachedFiles)
  puts result
rescue Exception => exception
  puts "Unable to create ticket: #{exception}"
end
```
