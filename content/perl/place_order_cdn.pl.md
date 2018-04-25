---
title: "place_order_cdn.pl"
description: "place_order_cdn.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
# Order a new CDN account
#
# Build a SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
# object for a new CDN account order and pass it to the SoftLayer_Product_Order
# API service to order it. In this script we'll order a pay as you go bandwidth
# and storage CDN account. See below for more details.
#
# This assumes you're using the SoftLayer API Perl client
# <http://github.com/softlayer/softlayer-api-perl-client>.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/placeOrder
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building a skeleton SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object
# containing the order you wish to place.
my $order_data = bless({
    "packageId" => 208, # The package id to order Content Delivery Network
    # The prices to order the CDN
    "prices" => [
        {
            "complexType" => "SoftLayer_Product_Item_Price",
            "id" => 1661 # CDN Pay as You Go Bandwidth 
        },
        {
            "complexType" => "SoftLayer_Product_Item_Price",
            "id" => 1670 # CDN No storage (origin pull)
        }
    ],
  "quantity" => 1, # We only want 1 firewall
},'slapi:SoftLayer_Container_Product_Order_Network_ContentDelivery_Account');

# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
#
# Once your order is placed it'll go through SoftLayer's provisioning process.
my $result = $softLayer_product_order->verifyOrder($order_data);
if ($result->fault) {
    die 'Unable to place the order. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The order was verified successfully");

```
