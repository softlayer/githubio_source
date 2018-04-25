---
title: "get_bandwith_image_by_date.rb"
description: "get_bandwith_image_by_date.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Bandwidth_GraphOutputs"
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```
# Retrieve bandwith image by date.
#
# Use this method when needing a bandwidth image for a single guest. It will gather the correct input parameters
# for the generic graphing utility based on the date ranges
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getBandwidthImageByDate
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

require 'rubygems'
require 'softlayer_api'
require 'awesome_print'
require 'date'

# The virtual guest id of the virtual guest object that's going to be retrieved to retrieve a bandwith image.
virtual_guest_id = 6032256
# An example value of year that may be used to create a DateTime
year = 2016
# An example value of month that may be used to create a DateTime
month = 6
# An example value of day that may be used to create a DateTime
day = 27
# A value added to day to represent a number of days in the future.
days_in_advance = 7
# A DateTIme value used as a date start point
start_date_time = DateTime.new(year, month, day)
# A DateTIme value used as a date end point
end_date_time = DateTime.new(year, month, day + days_in_advance)
# either public or private
network_type = 'public'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

virtual_guest_service = client['SoftLayer_Virtual_Guest']

begin
  container_bandwith_graph_outputs = virtual_guest_service.object_with_id(virtual_guest_id)
                                     .getBandwidthImageByDate(start_date_time, end_date_time, network_type)
  ap container_bandwith_graph_outputs
rescue StandardError => e
  p 'Error when executing the script...'
  $stdout.print(e.inspect)
end

```
