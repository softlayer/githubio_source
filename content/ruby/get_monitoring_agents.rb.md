---
title: "get_monitoring_agents.rb"
description: "get_monitoring_agents.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Retrieves the SoftLayer_Monitoring_Agent objects for a virtual_guest.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMonitoringAgents
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'

virtual_guest_id = 6032256

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  monitoring_agent = virtual_guest_service.object_with_id(virtual_guest_id)
                                          .getMonitoringAgents
  ap monitoring_agent
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
