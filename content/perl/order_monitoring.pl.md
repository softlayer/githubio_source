---
title: "order_monitoring.pl"
description: "order_monitoring.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
tags:
    - "monitoring"
---


```
# Order a Monitoring Package
# 
# Build a SoftLayer_Container_Product_Order_Monitoring_Package object for a new
# monitoring order and pass it to the SoftLayer_Product_Order API service to order it
# In this care we'll order a Basic (Hardware and OS) package with Basic Monitoring Package - Linux
# configuration for more details see below
# 
# Important manual pages:
# https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Monitoring_Package
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building an skeleton SoftLayer_Container_Product_Order_Monitoring_Package to the order
my $order_template = bless({
    'orderContainerType' => 'SoftLayer_Container_Product_Order_Monitoring_Package',
    'packageId' => 0, # The package id for order monitoring packages is 0
    'prices' => [
        { 'id' => 2302 } # This is the price for Monitoring Package - Basic ((Hardware and OS))
    ],
    'quantity' => 0,  # The quantity for order a service (in this case monitoring package) must be 0
    'sendQuoteEmailFlag' => True,
    'useHourlyPricing' => True,
    'virtualGuests' => [
        { 'id' => 4906034 } # The virtual guest id where you want add the monitoring package 
    ],
    'configurationTemplateGroups' => [
        { 'id' => 3 } # The template id for the monitoring group (in this case Basic Monitoring package for Unix/Linux operating system.)  
    ],      
},'slapi:SoftLayer_Container_Product_Order_Monitoring_Package');

# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
#
# Once your order is placed it'll go through SoftLayer's provisioning process.
my $result = $softLayer_product_order->verifyOrder($order_template);
if ( $result->fault ) {
  die 'Unable to create the server. ' . $result->faultstring;
}
print Dumper($result->result);
print ( "The order was verified successfully" );

```
