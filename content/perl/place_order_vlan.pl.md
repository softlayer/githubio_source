---
title: "place_order_vlan.pl"
description: "place_order_vlan.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Vlan"
tags:
    - "vlans"
---


```
# Example to create a new VLAN.
# 
# The script uses the placeOrder method to order
# a new VLAN with 32 static IP address
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib '/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building a skeleton SoftLayer_Container_Product_Order_Network_Vlan object
# to model the order for the new VLAN
my $order_template = bless({
    'orderContainerType' => 'SoftLayer_Container_Product_Order_Network_Vlan',
    'location' => 'AMSTERDAM',
    'packageId' => 0,
    # Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
    # much more than ids, but SoftLayer's ordering system only needs the price's id
    # to know what you want to order.
    # to get the list of valid prices for the package
    # use the SoftLayer_Product_Package:getItems method
    # e.g.
    # productPackageService = client['SoftLayer_Product_Package']
    # prices = productPackageService.getItems(id = packageID)
    'prices' => [
        {
            'complexType' => 'SoftLayer_Product_Item_Price',
            # The pice for the new Public Network Vlan
            'id' => 2018 
        },
                                
        {
            'complexType' => 'SoftLayer_Product_Item_Price',
            # The price for 32 Static Public IP Addresses
            'id' => 36716 
        }                                
    ],
    'quantity' => 1, 
    'sendQuoteEmailFlag' => True,
    'name" => "myVLANnew',
    # The router ID where the VLAN will be created
    # to get the list of routers in your account
    # use the SoftLayer_Account::getRouters method
    'routerId' => 117960     
},'slapi:SoftLayer_Container_Product_Order_Network_Vlan');

# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
# Once your order is placed it'll go through SoftLayer's provisioning process.
my $result = $softLayer_product_order->verifyOrder($order_template);
if ($result->fault) {
    die 'Unable to create the vlan. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The order was verified successfully");

```
