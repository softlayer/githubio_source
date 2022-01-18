---
title: "cancel_vlan.pl"
description: "cancel_vlan.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```perl
# Example to cancel a VLAN
#
# The script will get the Billing_Item id of the VLAN service
# then it will cancel the VLAN service
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use JSON;
use Data::Dumper;

# Your SoftLayer API key username.
my $username = 'set me';
my $key = 'set me';

# The VLAN id you wish to cancel
my $vlan_id = 563298;

# Creating a SoftLayer API client object
my $network_vlan_service = SoftLayer::API::SOAP->new('SoftLayer_Network_Vlan', undef, $username, $key);
my $billing_item_service = SoftLayer::API::SOAP->new('SoftLayer_Billing_Item', undef, $username, $key);

$network_vlan_service->setInitParameter($vlan_id);

# Declaring an object mask to get the billing item information
my $object_mask = "mask[id,billingItem.id]";
$network_vlan_service->setObjectMask($object_mask);

# Getting the Billing Item to cancel the VLAN service.
my $vlan = $network_vlan_service->getObject();
if ($vlan->fault) {
    die 'Unable to retrieve the vlan. ' . $vlan->faultstring;
}

# Canceling the VLAN service.
$billing_item_service->setInitParameter($vlan->result->{'billingItem'}->{'id'});
$result = $billing_item_service->cancelService();
if ($result->fault) {
    die 'Unable to cancel the vlan. ' . $result->faultstring;
}

print Dumper($result->result);

```
