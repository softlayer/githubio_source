---
title: "get_vlans_for_order.pl"
description: "get_vlans_for_order.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Order"
tags:
    - "vlans"
---


```
# Get available VLANs for a new order
# 
# The script makes a single call to SoftLayer_Product_Order::getVlans
# method to call the available VLANs for the configuration of an order
# for more details please see below.
# 
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/getVlans
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

my $location = 37473
my $package = 46
my $selected_items = 'port_speed=100'
my @vlans = (424830)

# Creating a SoftLayer API client object
my $product_order_service = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

my $result = $product_order_service->getVlans($location, $package, $selected_items, @vlans);

if ($result->fault) {
    die 'Unable to retrieve the VLANs. ' . $result->faultstring;
}

print Dumper($result->result);

```
