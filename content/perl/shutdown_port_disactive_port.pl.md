---
title: "shutdown_port_disactive_port.pl"
description: "shutdown_port_disactive_port.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```perl
# Sets the networks speed for a hardware devices
#
# This script makes a single call to the setPublicNetworkInterfaceSpeed() method
# to change the speed to public network or call the setPrivateNetworkInterfaceSpeed method
# to change the speed to private network.
#
# Important manual pages:
# http:'sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed
# http:'sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed
#
# See below for more details.
#
# License: http:'sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username.
my $username = 'set me';

# Your SoftLayer API key.
my $key = 'set me';

# The Id of the hardware you wish modified the networks.
my $hardware_id = 167407;

# The speed you wish configure if you want to disconnect the network you should set the value to '0'
my $new_speed_public_network = 10;
my $new_speed_private_network = 100;

# Declaring a new API service objects for:
my $hardware_server_service = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);

# It is not possible to update the two networks at same time, you need to update one and wait until
# the transaction is completed to update the second one.
$hardware_server_service->setInitParameter($hardware_id);
my $result = $hardware_server_service->setPublicNetworkInterfaceSpeed($new_speed_public_network);
print ("The public network speed has been modified? " . $result->result);
$result = $hardware_server_service->setPrivateNetworkInterfaceSpeed($new_speed_private_network);
print ("The private network speed has been modified? " . $result->result);

```
