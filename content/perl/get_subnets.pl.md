---
title: "get_subnets.pl"
description: "get_subnets.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
# Retrieve the subnets for a VLAN 
#
# Retrieve all the subnets for a determinate VLAN
# associated with a SoftLayer customer account 
# We do this with a call to the getSubnets() method in the 
# SoftLayer_Network_Vlan API service. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets
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

# The VLAN id you wish to see its subnets
my $result = $network_vlan_service->getSubnets();

# Sending the request to get the subnets
if ($result->fault) {
    die 'Unable to retrieve the subnets. ' . $result->faultstring;
    }
print Dumper($result->result);

```
