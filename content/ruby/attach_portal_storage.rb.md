---
title: "attach_portal_storage.rb"
description: "attach_portal_storage.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "portablestorages"
---


```
# Attach portal storage
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/attachDiskImage
#
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The portal storage ID which you wish to attach
image_id = 496_250_6

# The virtual guest Id where you wish to attach the portal storage
virtual_guest_id = 614_303_8

# Declaring the API client to use the SoftLayer_Virtual_Guest API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
virtual_guest_service = client.service_named('SoftLayer_Virtual_Guest')

begin
  result = virtual_guest_service.object_with_id(virtual_guest_id).attachDiskImage(image_id)
  pp result
rescue StandardError => exception
  puts "Unable to attach the portable storages.  #{exception}"
end

```
