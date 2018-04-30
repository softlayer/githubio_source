---
title: "activate_public_port.rb"
description: "activate_public_port.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Activate Public Port.
# It activates the public network port.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/activatePublicPort
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Set the server id.
server_id = 11498369

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

# Create a SoftLayer client
softlayer_client = SoftLayer::Client.new(:username => SL_API_USERNAME,
                                         :api_key => SL_API_KEY)
virtual_guest_service = softlayer_client['Virtual_Guest']

begin
  # Call the activatePublicPort method from SoftLayer_Virtual_Guest.
  server_ref = virtual_guest_service.object_with_id(server_id)
  result = server_ref.activatePublicPort
  p result

rescue StandardError => exception
  puts "Unable to activate the public port: #{exception}"
end

```
