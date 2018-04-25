---
title: "get_bandwidth_usage.pl"
description: "get_bandwidth_usage.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
# Retrieve a bandwidth usage for a list of  servers.
#
# The scripts returns the bandwidth usage from an arbitrary
# list of servers, the script makes a simple call to the
# Softlayer_Hardware_Server::getObject method using a object mask
# in order to get the bandwidth information.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
# http://sldn.softlayer.com/reference/datatype/SoftLayer_Hardware_Server/
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib '/path/to/client/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The list of server that wish to see the bandwidth usage
my @server_ids = ( 153851, 166391 );

# Creating a SoftLayer API client object
my $hardware_server = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);

# Adding an object mask to retrieve our hardware' related items such as its
# host name and currentBillableBandwidthUsage. Object masks
# can retrieve any information related to your object. See
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
my $object_mask = 'mask[hostname,currentBillableBandwidthUsage]';
$hardware_server->setObjectMask($object_mask);

my $total = 0.0;
for my $server_id (@server_ids) {
    $hardware_server->setInitParameter($server_id);
    my $result = $hardware_server->getObject();
    if ($result->fault) {
        die 'Unable to get bandwidth data. ' . $result->faultstring;
    }
    my $bandwidth_data = $result->result;
    print ($bandwidth_data->{'hostname'} . ": " . $bandwidth_data->{'currentBillableBandwidthUsage'} . "GB" , "\n");
    $total = $total + $bandwidth_data->{'currentBillableBandwidthUsage'};
}

print ("Total :" . $total , "\n");

```
