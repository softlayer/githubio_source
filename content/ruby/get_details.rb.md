---
title: "get_details.rb"
description: "get_details.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Get Virtual Guest details.
# It retrieves virtual guest information.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'

# Your SoftLayer API username.
SL_API_USERNAME = 'set me'

# Your SoftLayer API key.
SL_API_KEY = 'set me'

server_id = 10538555

# Creating the SoftLayer Client.
softlayer_client = SoftLayer::Client.new(:username => SL_API_USERNAME,
                                         :api_key => SL_API_KEY)

# Set the SoftLayer service to use.
vsi_service = softlayer_client['Virtual_Guest']

begin
  # Using extended objectMask in order to get the wanted information.
  mask_string = 'mask[operatingSystem.passwords,networkComponents,datacenter]'

  vsi_ref = vsi_service.object_with_id(server_id)

  # Make the call to retrieve the server details.
  result = vsi_ref.object_mask(mask_string).getObject
  p result

rescue StandardError => exception
  puts "Unable to get Virtual Server Instance's details: #{exception}"
end

```
