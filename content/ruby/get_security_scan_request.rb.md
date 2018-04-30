---
title: "get_security_scan_request.rb"
description: "get_security_scan_request.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "virtualservers"
---


```
# Retrieve a guest's vulnerability scan requests.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getSecurityScanRequests
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Security_Scanner_Request
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
  network_security_scanner_request = virtual_guest_service.object_with_id(virtual_guest_id)
                                                          .getSecurityScanRequests
  ap network_security_scanner_request
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end


```
