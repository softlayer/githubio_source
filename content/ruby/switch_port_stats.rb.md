---
title: "switch_port_stats.rb"
description: "switch_port_stats.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Network_Port_Statistic"
    - "SoftLayer_NetworkComponent"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Network_Component"
tags:
    - "vlans"
---


```
# Retrieve a list of switch port statistics for a server's network interfaces.
#
# This script makes a single call to the getPortStatistics() method in the
# SoftLayer_Network_Component API service
# (http://sldn.softlayer.com/reference/services/SoftLayer_NetworkComponent/getPortStatistics)
# for each of a server's network components to query port statistics for that
# interface from SoftLayer's switches. Port statistics are modeled by the
# SoftLayer__Container_Network_Port_Statistic data type
# (http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_Port_Statistic).
# See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Component
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Component/getPortStatistics
require 'softlayer_api'
require 'pp'

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# Your server's id. Call the getHardware() method in the SoftLayer_Account API
# service (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
# to get a list of your account's hardware records.
server_id = 152_782

# Switch port statistics are measured off the server's network components. Use
# an object mask to network component records along with our server record.
object_mask = 'mask[networkComponents]'

# Declare the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
hardware_server_service = client['SoftLayer_Hardware_Server']
network_component_service = client['SoftLayer_Network_Component']

begin
  # Make the call to retrieve our hardware record. Once we have that we can query
  # the server's network components.
  server = hardware_server_service.object_mask(object_mask).object_with_id(server_id).getObject
rescue StandardError => exception
  puts "Unable to retrieve server record. : #{exception}"
end

# Separate our network components for easier processing later.
network_components = server['networkComponents']
# Print out a simple report header.
print 'Switch port statistics for ' + server['fullyQualifiedDomainName']

# Loop through our server's network components. For each NIC make a call to the
# SoftLayer_Network_Component API service method getPortStatics() to get a list
# of switch port statistics retrieved from the switch on the other side of your
# NIC. Print a simple report per NIC.
network_components.each do |network_component|
  print network_component['id']
  # Skip the management network component.
  next if network_component['name'] == 'mgmt'

  begin
    # Retrieve switch port statistics for the NIC.
    stats = network_component_service.object_with_id(network_component['id']).getPortStatistics
    print stats
  rescue StandardError => exception
    puts "Unable to retrieve switchport statics for . : #{exception}"
  end
end

```
