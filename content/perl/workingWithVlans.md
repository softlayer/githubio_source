---
title: "Working with Vlans"
description: "A collection of CLI Examples on how to interact with Vlans."
date: "2022-04-21"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Account"
tags:
    - "vlans"
    - "order"
---

Read up on the [Perl article](/article/perl) for information on how to setup the CLI Framework to get this code to run easily.


## Placing Vlan order

This script makes a paginated API call to [SoftLayer_Product_Order::verifyOrder()](/reference/services/SoftLayer_Product_Order/verifyOrder/).


```perl
use lib '/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $apikey = 'set me';

# Building a skeleton SoftLayer_Container_Product_Order_Network_Vlan object
# to model the order for the new VLAN
my $order_template = bless({
	'orderContainerType' => 'SoftLayer_Container_Product_Order_Network_Vlan',
	'location' => 'AMSTERDAM',
	'packageId' => 571,		# ADDITIONAL_SERVICES_NETWORK_VLAN
	'prices' => [
		{
			'complexType' => 'SoftLayer_Product_Item_Price',
			'id' => 51775	# The pice for PUBLIC_NETWORK_VLAN
		} 
	],
	'quantity' => 1, 
	'sendQuoteEmailFlag' => True,
	'name' => 'A Vlan Name'
},'slapi:SoftLayer_Container_Product_Order_Network_Vlan');

# Creating a SoftLayer API client object
my $product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $apikey);

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. 
my $receipt = $product_order->verifyOrder($order_template);
if ($receipt->fault) {
	die 'Unable to create the vlan. ' . $receipt->faultstring;
}
print Dumper($receipt->result);
print ("The order was verified successfully");
```

## Canceling Vlan

This script makes a paginated API call to [SoftLayer_Billing_Item::cancelService()](/reference/services/SoftLayer_Billing_Item/cancelService/).


```perl
# Example to cancel a VLAN
#
# The script will get the Billing_Item id of the VLAN service
# then it will cancel the VLAN service
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use JSON;
use Data::Dumper;

# Your SoftLayer API key username.
my $username = 'set me';
my $key = 'set me';

# The VLAN id you wish to cancel
my $vlan_id = 563298;

# Creating a SoftLayer API client object
my $network_vlan_service = SoftLayer::API::SOAP->new('SoftLayer_Network_Vlan', undef, $username, $key);
my $billing_item_service = SoftLayer::API::SOAP->new('SoftLayer_Billing_Item', undef, $username, $key);

$network_vlan_service->setInitParameter($vlan_id);

# Declaring an object mask to get the billing item information
my $object_mask = "mask[id,billingItem.id]";
$network_vlan_service->setObjectMask($object_mask);

# Getting the Billing Item to cancel the VLAN service.
my $vlan = $network_vlan_service->getObject();
if ($vlan->fault) {
	die 'Unable to retrieve the vlan. ' . $vlan->faultstring;
}

# Canceling the VLAN service.
$billing_item_service->setInitParameter($vlan->result->{'billingItem'}->{'id'});
$result = $billing_item_service->cancelService();
if ($result->fault) {
	die 'Unable to cancel the vlan. ' . $result->faultstring;
}

print Dumper($result->result);

```


## Getting Vlan details

This script makes a paginated API call to [SoftLayer_Network_Vlan::getObject()](/reference/services/SoftLayer_Network_Vlan/getObject/).


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


## Listing Vlans

This script makes a paginated API call to [SoftLayer_Account::getNetworkVlans()](/reference/services/SoftLayer_Account/getNetworkVlans/).


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


## Getting available Vlans to order

This script makes a paginated API call to [SoftLayer_Product_Order::getVlans()](/reference/services/SoftLayer_Product_Order/getVlans/).

```perl
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
