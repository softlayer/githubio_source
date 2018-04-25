---
title: "get_firewall_list.pl"
description: "get_firewall_list.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Search"
    - "SoftLayer_Network_Vlan_Firewall"
tags:
    - "search"
---


```
# Get Firewall list using SoftLayer_Search::advancedSearch.
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

# Create a client to the SoftLayer_Search API service.
my $client = SoftLayer::API::SOAP->new($service_name, undef, $api_username, $api_key, $api_endpoint_url);

# The items with the following Device types should be displayed
# when applying the below filter:
# Firewall (Dedicated)
my $filter_data = '_objectType:SoftLayer_Network_Vlan_Firewall';

my $result = $client->advancedSearch($filter_data);

if ($result ->fault) {
    die 'Unable to get the item list. ' . $result ->faultstring;
}
print Dumper($result ->result);
```
