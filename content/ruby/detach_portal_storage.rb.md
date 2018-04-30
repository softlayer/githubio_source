---
title: "detach_portal_storage.rb"
description: "detach_portal_storage.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "portablestorages"
---


```
# Detach portal storage
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/detachDiskImage
#
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The portal storage ID which you wish to attach
image_id = 482_714_4
# The virtual guest Id where you wish to attach the portal storage
virtual_guest_id = 566_006_6

# Declaring the API client to use the SoftLayer_Virtual_Guest API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
virtual_guest_service = client.service_named('SoftLayer_Virtual_Guest')

begin
  result = virtual_guest_service.object_with_id(virtual_guest_id).detachDiskImage(image_id)
  pp result
rescue StandardError => exception
  puts "Unable to detach the portable storages.  #{exception}"
end

```
