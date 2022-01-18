---
title: "delete_network_monitoring.pl"
description: "delete_network_monitoring.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```perl
# Delete network monitoring
#
# The script makes a single call to SoftLayer_Network_Monitor_Version1_Query_Host::deleteObject
# method to delete the network monitoring for more information see below
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObject
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The id of the newtwork monitor you wish to delete
# To get the list of network monitors
# my $virtual_guest_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $username, $key);
# my $virtual_guest_id =  7698842;
# $virtual_guest_service->setInitParameter($virtual_guest_id);
# my $network_monitors = $virtual_guest_service->getNetworkMonitors();
# print Dumper($network_monitors->result);
# print (network_monitors)
my $id_network_monitoring_to_delete = 1789133;

# Creating a SoftLayer API client object
my $user_customer_notificiation = SoftLayer::API::SOAP->new('SoftLayer_Network_Monitor_Version1_Query_Host', undef, $username, $key);

$user_customer_notificiation->setInitParameter($id_network_monitoring_to_delete);

# Sending the request to delete the object
my $result = $user_customer_notificiation->deleteObject();

if ($result->fault) {
    die 'Unable to delete network monitoring. ' . $result->faultstring;
}
print Dumper($result->result);

```
