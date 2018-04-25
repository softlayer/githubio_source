---
title: "get_server_details.rb"
description: "get_server_details.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
# Get server details
#
# Retrieve a list of hardware and print a report with server hostname, domain,
# login info, network, CPU, and RAM details.
# This script makes a single call to the getHardware() method in the
# SoftLayer_Account API service
# (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
# and uses an object mask to retrieve related information. It uses the
# SoftLayer API Ruby client
# <https://github.com/softlayer/softlayer-ruby> to handle API calls.
# See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
require 'rubygems'
require 'softlayer_api'
require 'json'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declaring the API client
client = SoftLayer::Client.new(username: USERNAME, api_key: API_KEY)
account_service = client['SoftLayer_Account']

# Add an object mask to retrieve our hardwares' related items such as its
# operating system, hardware components, and network components. Object masks
# can retrieve any information related to your object. See
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
object_mask = 'mask[processors, processorCount, memory, memoryCount, networkComponents, primaryIpAddress, operatingSystem[passwords]]'

begin
  # Make the call to retrieve our hardware records.
  hardware_list = account_service.object_mask(object_mask).getHardware
rescue StandardError => exception
  # If there was an error returned from the SoftLayer API then bomb out with the
  # error message.
  puts "Unable to list the servers: #{exception}"
end

hardware_list.each do |hardware|
  # Puts hardware
  passwords = hardware['operatingSystem']['passwords'][0]
  networks = hardware['networkComponents']
  public_mac_address = 'not found'
  private_mac_address = 'not found'
  networks.each do |network|
    # SoftLayer uses eth0 on the private network and eth1 on the public
    # network.
    if network['name'] == 'eth' && network['port'] == 0
      private_mac_address = network['macAddress']
    else
      if network['name'] == 'eth' && network['port'] == 1
        public_mac_address = network['macAddress']
      end
    end
  end

  # Hardware can only have like processors in them, so use the first item in
  # the processors array to get the type of processor in the server.
  processor_type = hardware['processors'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['capacity'] + \
                   hardware['processors'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['units'] + ' ' + \
                   hardware['processors'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['description']

  # Treat memory the same way we did processors.
  memory_type = hardware['memory'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['capacity'] + \
                hardware['memory'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['units'] + ' ' + \
                hardware['memory'][0]['hardwareComponentModel']['hardwareGenericComponentModel']['description']

  # All done! Print hardware info.
  puts 'Hostname: ' + hardware['hostname']
  puts 'Domain: ' + hardware['domain']
  puts 'Login: ' + passwords['username'] + '/' + passwords['password']
  puts 'Public IP Address: ' + hardware['primaryIpAddress']
  puts 'Public MAC Address: ' + public_mac_address
  puts 'Private IP Address: ' + hardware['privateIpAddress']
  puts 'Private MAC Address: ' + private_mac_address
  puts 'CPUs: ' + (hardware['processorCount']).to_s + 'x ' + processor_type
  puts 'RAM: ' + (hardware['memoryCount']).to_s + 'x ' + memory_type
  puts ' '
end

```
