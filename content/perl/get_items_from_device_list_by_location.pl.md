---
title: "get_items_from_device_list_by_location.pl"
description: "get_items_from_device_list_by_location.pl"
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
# Get all items from Device according to an specific location.
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

# Set the location name to filter the items
my $location = 'Dallas 5';

# Create a client to the SoftLayer_Search API service.
my $client = SoftLayer::API::SOAP->new($service_name, undef, $api_username, $api_key, $api_endpoint_url);

# The items with the following Device types should be displayed
# when applying the below filter:
# Bar Metal Server, Virtual Server, Firewall, Gateway Member, Netscaler,KVM/IP
my $filter_data = 'datacenter.longName: "' . $location . '"'.
				' _objectType:SoftLayer_Hardware,'.
				'SoftLayer_Virtual_Guest,'.
				'SoftLayer_Network_Vlan_Firewall,'.
				'SoftLayer_Network_Application_Delivery_Controller';

my $result = $client->advancedSearch($filter_data);

if ($result ->fault) {
    die 'Unable to get the item list when filtering by location. ' . $result ->faultstring;
}
print Dumper($result ->result);
```
