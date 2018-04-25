---
title: "get_items_filtered_by_private_ip.pl"
description: "get_items_filtered_by_private_ip.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Vlan_Firewall"
tags:
    - "search"
---


```
# Get items from "Portal>Device List" filtered by Private IP
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Search/advancedSearch
#
# License: http://sldn.softlayer.com/article/License
use lib 'C:\Perl_Modules\softlayer-api-perl-client-master';
use Data::Dumper;
use SoftLayer::API::SOAP;
use strict;
 
# Set your SoftLayer API username and key.
my $api_username = 'set me';
my $api_key = 'set me';
my $service_name = 'SoftLayer_Search';
my $api_endpoint_url = 'https://api.softlayer.com/soap/v3.1/';

# Set the "private IP" to filter the items
my $private_ip = '10.102.52.131';

# Create a client to the SoftLayer_Search API service.
my $client = SoftLayer::API::SOAP->new($service_name, undef, $api_username, $api_key, $api_endpoint_url);

# The items with the following Device types should be displayed
# when applying the below filter:
# Bar Metal Server, Virtual Server, Firewall, Gateway Member, Netscaler,KVM/IP
my $filter_data = 'primaryBackendIpAddress: ' . $private_ip . 
				'_objectType:SoftLayer_Hardware,'.
				'SoftLayer_Virtual_Guest,'.
				'SoftLayer_Network_Vlan_Firewall,'.
				'SoftLayer_Network_Application_Delivery_Controller';

my $result = $client->advancedSearch($filter_data);

if ($result ->fault) {
    die 'Unable to get the items according to "private IP" filter. ' . $result ->faultstring;
}
print Dumper($result ->result);
```
