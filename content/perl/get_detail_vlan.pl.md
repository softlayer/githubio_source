---
title: "get_detail_vlan.pl"
description: "get_detail_vlan.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```perl
# Retrieve VLAN details such as primary router and subnet.
#
# Retrieving the primary router and subnet for a determinate VLAN
# associated with a SoftLayer customer account 
# We do this with a call to the getObject() method in the 
# SoftLayer_Network_Vlan API service using an object mask to retrieve  
# associated subnets and primary router records. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use JSON;
use Data::Dumper;

# Your SoftLayer API key and username.
my $username = 'set me';
my $key = 'set me';

# The VLAN id you wish to see its details
my $vlan_id = 557984;

# Creating a SoftLayer API client object
my $network_vlan_service = SoftLayer::API::SOAP->new('SoftLayer_Network_Vlan', undef, $username, $key);

$network_vlan_service->setInitParameter($vlan_id);

# Declaring an object mask to get more information about the VLANs
# such as the primaryRouter and the subnets
my $object_mask = "mask[primaryRouter, subnets[ipAddresses]]";
$network_vlan_service->setObjectMask($object_mask);

# Send the request to get the VLANs
my $result = $network_vlan_service->getObject();

if ($result->fault) {
    die 'Unable to retrieve the VLAN details ' . $result->faultstring;
}
print Dumper($result->result);

```
