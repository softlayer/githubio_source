---
title: "get_gateway_member_items_using_search.pl"
description: "get_gateway_member_items_using_search.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
tags:
    - "search"
---


```perl
# Get Gateway Member list using SoftLayer_Search::advancedSearch.
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
my $service_name ='SoftLayer_Search';
my $api_endpoint_url = 'https://api.softlayer.com/soap/v3.1/';

# Create a client to the SoftLayer_Search API service.
my $client = SoftLayer::API::SOAP->new($service_name, undef, $api_username, $api_key, $api_endpoint_url);

# The items with the following Device types should be displayed
# when applying the below filter: Gateway Member
my $filter_data = 'networkGatewayMemberFlag:1 _objectType:SoftLayer_Hardware';

my $result = $client->advancedSearch($filter_data);

if ($result ->fault) {
    die 'Unable to get the item list. ' . $result ->faultstring;
}
print Dumper($result ->result);

```
