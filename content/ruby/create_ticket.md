---
title: "Creating a support ticket"
description: "Create a standard support ticket assigned to your user"
date: "2016-08-22"
classes: ["SoftLayer_Ticket_Subject", "SoftLayer_Ticket"]
tags:
    - "ticket"
---

Standard support tickets' titles must be selected from a pre-determined list of ticket subjects, defined in the [SoftLayer_Ticket_Subject](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject) service. The following example will output all of the Ticket Subjects:

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

subjects = client['SoftLayer_Ticket_Subject']
getSubjects = subjects.getAllObjects()

pp getSubjects
```

Once you have the Ticket Subject ID you can pass it to [createStandardTicket](http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createStandardTicket). In the following example we are opening a ticket under the subject Hardware Firewall Question (ID 1121).

```ruby
require 'softlayer_api'
require 'pp'

# Credentials to the API are read from a configuration file by default.
# See https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L44
client = SoftLayer::Client.new(:timeout => 120)

ticketTemplate = {
	'subjectId' => 1121,
	'assignedUserId' => xxxxx,
}

content = "Content of the ticket goes here."

ticket = client['SoftLayer_Ticket']
createTicket = ticket.createStandardTicket(ticketTemplate, content)

pp createTicket

```
