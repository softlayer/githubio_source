---
title: "edit_details.rb"
description: "edit_details.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Edit details of a Virtual Guest.
# This script edits a computing instance's properties.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'rubygems'
require 'softlayer_api'

# Set the server id that you wish to edit.
server_id = 11498360

new_hostname_update = 'vsi-test-edited.softlayer.com'
notes = 'edited from api'

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

softlayer_client = SoftLayer::Client.new(:username => SL_API_USERNAME,
                                         :api_key => SL_API_KEY)

server = SoftLayer::VirtualServer.server_with_id(server_id, :client => softlayer_client)

begin
  # Example: we want to edit the "hostname" and add some "notes".
  server.set_hostname!(new_hostname_update)
  server.notes = notes
  p 'The server was edited successfully'

rescue StandardError => exception
  p "Unable to edit Virtual Guest's details: #{exception}"
end


```
