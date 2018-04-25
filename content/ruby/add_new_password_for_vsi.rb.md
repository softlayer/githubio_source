---
title: "add_new_password_for_vsi.rb"
description: "add_new_password_for_vsi.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Software_Component_Password"
tags:
    - "virtualservers"
---


```
# Change user and password for a VSI.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Account
# https://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_Password
# https://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_Password/createObject
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

vsi_host_name = 'test'
new_pass = 'new pass'
new_username = 'new pass'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client.service_named('SoftLayer_Account')
component_password_service = client.service_named('SoftLayer_Software_Component_Password')
# An object mask to get more details about the virtual guest such as softwarecomponents, passwords and soft
object_mask = 'mask[softwareComponents[passwords]]'

# Getting all virtual guest in the account
virtual_guests = account_service.object_mask(object_mask).getVirtualGuests

begin
  virtual_guests.each do |virtual_guest|
    if virtual_guest['hostname'] == vsi_host_name
      # Getting the virtual guest's softwareId in order to add a new password
      # notice that the user is not created in the server
      # it is just stored in the softlayer's database
      # you need to create the user in the server manually.
      software_id = virtual_guest['softwareComponents'][0]['passwords'][0]['softwareId']
      result = component_password_service.createObject(
        'password' => new_pass,
        'username' => new_username,
        'softwareId' => software_id
      )
      print result
    end
  end
rescue StandardError => exception
  puts "Unable to change the password: #{exception}"
end

```
