---
title: "cancel_server.pl"
description: "cancel_server.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item_Hardware"
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```perl
# Cancel servers from a list of IPs
#
# This script looks for a server with a determinate IP address and delete it.
#
# It makes a single call to the cancelService() method in the
# SoftLayer_Billing_Item API service
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item_Hardware
# http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Adding an object mask to retrieve our billing items related to the servers
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
my $object_mask = 'mask[billingItem]';

# The list of IPs from the servers you wish to cancel
my @ips_to_cancel = ('1.1.1.1', '2.2.2.2');

# Declaring a new API service object for the
# SoftLayer_Account API service
# SoftLayer_Billing_Item service
my $hardware_server_service = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);
my $billing_item_service = SoftLayer::API::SOAP->new('SoftLayer_Billing_Item', undef, $username, $key);

# Making the call to retrieve our hardware records along with their billing item.
# Setting the init parameter with the server Id
$hardware_server_service->setObjectMask($object_mask);

for my $ip_to_cancel (@ips_to_cancel) {
    my $server = $hardware_server_service->findByIpAddress($ip_to_cancel);
    if ($server->fault) {
        die 'Unable to get the server. ' . $server->faultstring;
    }
    my $billing_id = $server->result->{'billingItem'}->{'id'};
    $billing_item_service->setInitParameter($billing_id);
    my $result = $billing_item_service->cancelService();
    if ($result->fault) {
        die 'Unable to cancel the server. ' . $server->faultstring;
    }
    print Dumper($result->result);
}

```
