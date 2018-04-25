---
title: "order_evault.pl"
description: "order_evault.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
tags:
    - "evault"
---


```
# Order a Evault
# 
# Building a SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
# object for a new Evault order and pass it to the SoftLayer_Product_Order
# for more information see below:
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

my $order_template = {
    "complexType" => "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault",
    
    # Building a skeleton SoftLayer_Hardware object.
    # the object contains the hardware id of the
    # Bare Metal server which will contain the Evault
    # If you want use a Virtual Server instead a
    # Bare Metal server build a skeleton SoftLayer_Virtual_Guest object
    "virtualGuests" => [
        {
            "complexType" => "SoftLayer_Virtual_Guest",
            "id" => 4241550
        }
    ],
    # The location for the Evault
    "location" => "DALLAS06",
    "packageId" => 0,
    # Building a skeleton SoftLayer_Product_Item_Price object.
    # The object contains the price ID of the Evaul device
    # you wish order.
    "prices" => [
        {
            "complexType" => "SoftLayer_Product_Item_Price",
            "id" => 1045
        }
    ],    
    "quantity" => 1   
};

# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

# verifyOrder() will check your order for errors. Replace this with a call
# to placeOrder() when you're ready to order. Both calls return a receipt
# object that you can use for your records.
# Once your order is placed it'll go through SoftLayer's approval and
# provisioning process.  
my $result = $softLayer_product_order->verifyOrder($order_template);
if ($result->fault) {
    die 'Unable to create the server. ' . $result->faultstring;
    }
print Dumper($result->result);
print ("The order was verified successfully");

```
