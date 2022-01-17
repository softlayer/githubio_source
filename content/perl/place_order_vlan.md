---
title: "Order a Vlan"
description: "Order a Network Vlan device"
date: "2019-03-18"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Vlan"
tags:
    - "vlans"
    - "order"
---


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
    'packageId' => 571,    # ADDITIONAL_SERVICES_NETWORK_VLAN
    'prices' => [
        {
            'complexType' => 'SoftLayer_Product_Item_Price',            
            'id' => 51775 # The pice for PUBLIC_NETWORK_VLAN
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
