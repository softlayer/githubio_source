---
title: "order_dedicated_firewall.pl"
description: "order_dedicated_firewall.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "firewall"
---


```perl
# 
# Order dedicated firewall
# 
# The script calls the SoftLayer_Product_Order::placeOrder method to
# order a firewall.
# for more information see below.
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# license <http://sldn.softlayer.com/article/License>
# author SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building a skeleton SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated object
# containing the order you wish to place.
my $order_data = bless({
    "orderContainerType" => "SoftLayer_Container_Product_Order_Network_Protection_Firewall",
    "virtualGuests" => [
        {
            "complexType" => "SoftLayer_Virtual_Guest",
            "id" => 6674100 # The virtual Guest id where you wish add a firewall.
        }
    ],
    "location" => 168642, # The location for the firewall in this case "San Jose 1"
    "packageId" => 0, # The package id to order firewalls
    # The prices to order the Firewall
    "prices" => [
        {
            "complexType" => "SoftLayer_Product_Item_Price",
            "id" => 410 # Price to 10Mbps Hardware Firewall 
        }
    ],
    "quantity" => 1, # We only want 1 firewall
},'slapi:SoftLayer_Container_Product_Order_Network_Protection_Firewall');

# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
# Once your order is placed it'll go through SoftLayer's provisioning process.
my $result = $softLayer_product_order->verifyOrder($order_data);
if ($result->fault) {
    die 'Unable to create the server. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The order was verified successfully");

```
