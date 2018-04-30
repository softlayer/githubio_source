---
title: "get_brandwidth_graph.rb"
description: "get_brandwidth_graph.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Bandwidth_GraphOutputs"
    - "SoftLayer_Container_Bandwidth_GraphOutput"
    - "SoftLayer_Account"
    - "SoftLayer_Metric_Tracking_Object"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
#
# Retrieve a bandwidth graph for a single server.
#
# Retrieve a bandwidth graph for a single server for an arbitrary start and
# end date, specifying graph size and other graphing options. We can do this
# with two calls to the SoftLayer API.
#
# Counter data such as bandwidth counters and CCI resource use are stored in
# a server's metric tracking object. Our first call retrieves that server's
# tracking object record. The second call is to the tracking object service
# which will generate a PNG image of our bandwidth graph.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutput
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The id number of the server whose graph you wish to retrieve. Call the
# getHardware() method in the SoftLayer_Account API service to retrieve a list
# of the servers on your account.
server_id  = 153_851
# The date at which you wish to start graphing bandwidth.
start_date = '2010-10-1'
# The date at which you wish to end graphing bandwidth.
end_date = '2014-8-11'
# Whether to get a graph for 'public' or 'private' bandwidth usage.
graph_type = 'public'
# The height of the text in the bandwidth graph in pixels.
font_size = 8
# The width of the graph to retrieve in pixels.
graph_width = 827
graph_height = 273
hide_time_zone = true

client = SoftLayer::Client.new(username:  USERNAME, api_key: API_KEY)

hardware_service = client.service_named('Hardware_Server')
metric_tracking_object = client.service_named('SoftLayer_Metric_Tracking_Object')

begin
  tracking_object = hardware_service.object_with_id(server_id).getMetricTrackingObject
rescue StandardError => exception
  puts "Unable to retrieve the metric tracking object: #{exception}"
end

begin
  # getBandwidthGraph() returns a SoftLayer_Container_Bandwidth_GraphOutputs
  # object. The contents of the bandwidth image is in $image->graphImage.
  # From here you can write it to the file system, display it to a web
  # browser, or run other functions on it.
  image = metric_tracking_object.object_with_id(tracking_object['id']).getBandwidthGraph(start_date, end_date, graph_type, font_size, graph_width, graph_height, hide_time_zone)
  print 'Image retrieved!'
rescue StandardError => exception
  puts "Unable to retrieve bandwidth image: #{exception}"
end

```
