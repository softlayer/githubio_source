---
title: "order_Vyatta.pl"
description: "order_Vyatta.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance"
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Hardware_Server"
tags:
    - "viyatta"
---


```perl
# Order a Network Gateway Appliance (Vyatta)
#
# The script orders a (Vyatta) high availability pair
# it uses the SoftLayer_Product_Order::placeOrder to make the order
# For more information see below:
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building a skeleton SoftLayer_Container_Product_Order object.
# the object contains the configuration for the Vyatta server
# such as the quantity, the location, etc. 
my $product_order= {
    # The number of servers you wish to order.
    # If you wish a high availability  pair you must specify 2 as quantity.
    "quantity" => 2,
    # Building a skeleton SoftLayer_Hardware_Server object to model the hostname and
    # domain we want for our server. If you set quantity greater than 1 then you
    # need to define one hostname/domain pair per server you wish to order.
    "hardware" => [
        {
            "hostname" => "vyattagw", 
            "domain" => "test.com"
        },
        {
            "hostname" => "vyattagw2", 
            "domain" => "test.com"
        }  
    ],
    # Where you'd like your new server provisioned.
    # this can either be the id of the datacenter
    # you wish your new server to be provisioned in
    "location" => 265592,
    # The id of the SoftLayer_Product_Package you wish to order.
    # In this case the Network Gateway Appliance (Vyatta) package id is 174.
    "packageId" => 174,      
    # Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
    # much more than ids, but SoftLayer's ordering system only needs the price's id
    # to know what you want to order.

    # Every item in SoftLayer's product catalog is assigned an id. Use these ids
    # to tell the SoftLayer API which options you want in your new server. Use
    # the getActivePackages() method in the SoftLayer_Account API service to get
    # a list of available item and price options per available package.
    "prices"=>[
        { "id" => 13738 },
        { "id" => 21010 },
        { "id" => 36044 },
        { "id" => 876 },
        { "id" => 1267 },
        { "id" => 342 },
        { "id" => 273 },
        { "id" => 17129 },
        { "id" => 55 },
        { "id" => 58 },
        { "id" => 420 },
        { "id" => 418 },
        { "id" => 21 },
        { "id" => 57 },
        { "id" => 906 }
    ]  
};

# Building a skeleton SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance object.
# this object contains the order for the Vyatta server.
my $order_data = {
    "orderContainers" => [
        $product_order
    ]
};
  
# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key); 

# verifyOrder() will check your order for errors. Replace this with a call
# to placeOrder() when you're ready to order. Both calls return a receipt
# object that you can use for your records.
#
# Once your order is placed it'll go through SoftLayer's approval and
# provisioning process.   
my $result = $softLayer_product_order->verifyOrder($order_data);
if ($result->fault) {
    die 'Unable to create the server. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The order was verified successfully");

```
