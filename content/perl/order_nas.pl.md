---
title: "order_nas.pl"
description: "order_nas.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order_Network_Storage_Nas"
    - "SoftLayer_Product_Order"
tags:
    - "nas"
---


```perl
# Order a NAS
# 
# Build a SoftLayer_Container_Product_Order_Network_Storage_Nas
# object for a new CDN account order and pass it to the SoftLayer_Product_Order
# API service to order it. In this script we'll order a NAS. See below for more details.
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Nas
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building a skeleton SoftLayer_Container_Product_Order_Network_Storage_Nas object
# containing the order you wish to place.
my $order_data = bless({
    'packageId' => 216, # The package id to order NAS
    'location' => 'AMSTERDAM',
    # The prices to order the NAS
    'prices' => [
        {
            'complexType' => 'SoftLayer_Product_Item_Price',
            'id' => 508 # 20 GB NAS
        }
    ],
    'quantity' => 1, # We only want 1 firewall
    'privateCloudOrderFlag' => False,
},'slapi:SoftLayer_Container_Product_Order_Network_Storage_Nas');

# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
# Once your order is placed it'll go through SoftLayer's provisioning process.
my $result = $softLayer_product_order->verifyOrder($order_data);
if ($result->fault) {
    die 'Unable to order. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The order was verified successfully");

```
