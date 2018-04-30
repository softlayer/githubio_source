---
title: "order_portable_storage.pl"
description: "order_portable_storage.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Disk_Image"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "portablestorage"
---


```
# Order a portal storage
# 
# The script orders a portal storage device, it makes a single call to
# SoftLayer_Product_Order::placeOrder method.
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Disk_Image
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building an skeleton SoftLayer_Container_Product_Order_Virtual_Disk_Image to the order
my $order_template = bless({
  'orderContainerType' => 'SoftLayer_Container_Product_Order_Virtual_Disk_Image',
  'location' => 'SANJOSE',
  # The package for order portable storage
  'packageId' => 198,
  'diskDescription' => 'test portable storage',   
  'prices' => [
    {
      # The prices for the portable storage
      # to see the list of prices available for the package
      # use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
      # e.g.
      # client = SoftLayer::Client.new(:username => user,:api_key => api_key)
      # productPackageService = client.service_named("Softlayer_Product_Package")
      # packageID = 198
      # result = productPackageService.object_with_id(packageID).getItems()
      'id' => 21861
    }
  ],      
},'slapi:SoftLayer_Container_Product_Order_Virtual_Disk_Image');

# Creating a SoftLayer API client object
my $softLayer_product_order = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key);

# Verifying the order when you are ready to create the
# portal storage replace "verifyOrder" by "placeOrder"
my $result = $softLayer_product_order->verifyOrder($order_template);
if ($result->fault) {
  die 'Unable to create the order. ' . $result->faultstring;
}
print Dumper($result->result);
print ('The order was verified successfully');

```
