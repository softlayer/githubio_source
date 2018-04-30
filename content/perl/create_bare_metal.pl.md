---
title: "create_bare_metal.pl"
description: "create_bare_metal.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
# Order a new server.
#
# Building a SoftLayer_Container_Product_Order object for a new
# server order and pass it to the SoftLayer_Product_Order API service to order
# it. In this care we'll order a Xeon 3460 server with 2G RAM, 100mbit NICs,
# 2000GB bandwidth, a 500G SATA drive, CentOS 5 32-bit, and default server
# order options. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
# http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
#
# License <http://sldn.softlayer.com/article/License>
# Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib '/path/to/client/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username.
my $username = 'set me';

# Your SoftLayer API key.
my $key = 'set me too';

# The number of servers you wish to order in this configuration.
my $quantity = 1;

# Where you'd like your new server provisioned.
# This can either be the id of the datacenter you wish your new server to be
# provisioned in or the string 'FIRST_AVAILABLE' if you have no preference
# where your server is provisioned.
# Location id 3     = Dallas
# Location id 18171 = Seattle
# Location id 37473 = Washington, D.C.
my $location = 'FIRST_AVAILABLE';

# The id of the SoftLayer_Product_Package you wish to order.
# In this case the Intel Xeon 3460's package id is 145.
my $package_id = 145;

# Building a skeleton SoftLayer_Hardware_Server object to model the hostname and
# domain we want for our server. If you set quantity greater than 1 then you
# need to define one hostname/domain pair per server you wish to order.
my @hardware = (
    {
        'hostname' => 'test', # The hostname of the server you wish to order.
        'domain' => 'example.org' # The domain name of the server you wish to order.
    }
);

# Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
# much more than ids, but SoftLayer's ordering system only needs the price's id
# to know what you want to order.

# Every item in SoftLayer's product catalog is assigned an id. Use these ids
# to tell the SoftLayer API which options you want in your new server. Use
# the getActivePackages() method in the SoftLayer_Account API service to get
# a list of available item and price options per available package.
my @prices = (
    { 'id' => 17231 } , # Single Processor Quad Core Xeon 3460 - 2.80GHz (Lynnfield) - 1 x 8MB cache w/HT
    { 'id' => 637 }, # 2 GB DDR2 667
    { 'id' => 682 }, # CentOS 5.x (32 bit)
    { 'id' => 876 }, # 2 GB DDR2 667
    { 'id' => 19087 }, # 500GB SATA II
    { 'id' => 342 }, # 20000 GB Bandwidth
    { 'id' => 273 }, # 100 Mbps Public & Private Network Uplinks
    { 'id' => 55 }, # Host Ping
    { 'id' => 58 }, # Automated Notification
    { 'id' => 420 }, # Unlimited SSL VPN Users & 1 PPTP VPN User per account
    { 'id' => 418 }, # Nessus Vulnerability Assessment & Reporting
    { 'id' => 21 }, # 1 IP Address
    { 'id' => 57 }, # Email and Ticket
    { 'id' => 906 } # Reboot / KVM over IP
);

# Building a skeleton SoftLayer_Container_Product_Order_Hardware_Server object
# containing the order you wish to place.
my $order_template = {
    'quantity' => $quantity,
    'location' => $location,
    'packageId' => $package_id,
    'prices' => [ @prices ],
    'hardware' => [ @hardware ]
};

# Declaring the API client to use the SoftLayer_Product_Order API service
my $client = SoftLayer::API::SOAP->new('SoftLayer_Product_Order', undef, $username, $key,$endpoint);

# verifyOrder() will check your order for errors. Replace this with a call to
# placeOrder() when you're ready to order. Both calls return a receipt object
# that you can use for your records.
#
# Once your order is placed it'll go through SoftLayer's provisioning process.
# When it's done you'll have a new SoftLayer_Virtual_Guest object and CCI ready
# to use.
my $receipt = $client->verifyOrder($order_template);

if ($receipt->fault) {
    die 'There was an error in your order. ' . $receipt->faultstring;
}

# Pretty print the order receipt.
print Dumper($receipt->result);

```
