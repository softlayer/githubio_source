---
title: "get_template_group_monitoring.rb"
description: "get_template_group_monitoring.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
tags:
    - "monitoring"
---


```
# Get the SoftLayer_Monitoring_Agent_Configuration_Template_Group
# for use them in a Monitor package order
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'softlayer_api'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The package id for Monitoring package
package_id = 0

# Declare the API client to use the SoftLayer_Monitoring_Agent_Configuration_Template_Group API service
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
template_service = client.service_named('SoftLayer_Monitoring_Agent_Configuration_Template_Group')

begin
  # Gets the available templates
  templates = template_service.getConfigurationGroups(package_id)
  puts templates
rescue StandardError => exception
  puts "Unable to get templates: #{exception}"
end

```
