---
title: "get_vlan.pl"
description: "get_vlan.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```perl
# Retrieve account VLAN and subnet information.
#
# Retrieving a list of all VLANs associated with a SoftLayer customer account
# and print a simple report detailing these VLANs and the subnets assigned to
# them. We do this with a call to the getNetworkVlans() method in the
# SoftLayer_Account API service using an object mask to retrieve the VLANs'
# associated subnets and primary router records. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans
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

# Creating a SoftLayer API client object
my $account_service = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $username, $key);

# Declaring an object mask to get more information about the vlans
# such as the primaryRouter and the subnets
my $object_mask = "mask[primaryRouter, subnets[ipAddresses]]";
$account_service->setObjectMask($object_mask);

# Sending the request to get the vlans
my $result = $account_service->getNetworkVlans();

if ($result->fault) {
    die 'Unable to retrieve the VLANs. ' . $result->faultstring;
}
print Dumper($result->result);

```
