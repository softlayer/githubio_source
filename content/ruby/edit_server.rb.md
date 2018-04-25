---
title: "edit_server.rb"
description: "edit_server.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
#
# Edit a server's basic information
#
# Change the notes property for a single server record to the sentence "This
# is my fastest server!" using the editObject() method in the
# SoftLayer_Hardware_Server API service. See below for more details.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/editObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server/
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The name of the server we wish to edit.
server_name = 'set me'

# Define the new local properties to set.
#
# A SoftLayer_Hardware_Server record has a few local properties that you can
# change via the API. Every service's editObject() method takes a single
# parameter, a skeleton object that only defines the properties we wish to
# change. While we're only editing a server's notes in this example you can
# also use editObject() to edit the server's hostname and domain record.
edit_template = {
  'notes' => 'This is my fastest server!'
}

hardware_id = '12321'

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']
hardware_server_service = client['SoftLayer_Hardware_Server']

begin
  # Make the call to retrieve our hardware records.
  hardware_list = account_service.getHardware
rescue StandardError => exception
  # If there was an error returned from the SoftLayer API then bomb out with the
  # error message.
  puts "Unable to list the servers: #{exception}"
end

# Looking for the server name to get its id
hardware_list.each do |hardware|
  hardware_id = hardware['id'] if hardware['hostname'] == server_name
end

begin
  # Edit our server record.
  result = hardware_server_service.object_with_id(hardware_id).editObject(edit_template)
  puts 'Server edited'
  print result
rescue StandardError => exception
  puts "Unable to edit the server: #{exception}"
end

```
