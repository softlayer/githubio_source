---
title: "get_items_from_device_list_using_multiple_filters.pl"
description: "get_items_from_device_list_using_multiple_filters.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Search"
    - "SoftLayer_Hardware"
tags:
    - "search"
---


```
# Get items from "Portal>Device List" filtered by multiple filters
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

# Setting some Filters:
#     Devicename: ccnewtork3306vddal06.softlayer.local
#     Location: Dallas 6
#     Devicetype: Gateway Member
#     PrivateIp: 10.107.141.195
my $location = 'Dallas 6';
my $device_name = 'ccnewtork3306vddal06.softlayer.local';
my $private_ip = '10.107.141.195';

# Create a client to the SoftLayer_Search API service.
my $client = SoftLayer::API::SOAP->new($service_name, undef, $api_username, $api_key, $api_endpoint_url);

my $filter_data = 'networkGatewayMemberFlag:"1" '.
                  '& datacenter.longName:"'.$location .'"'.
                  '& primaryBackendIpAddress:'.$private_ip.
                  '& fullyQualifiedDomainName:'. $device_name.
                  '_objectType:SoftLayer_Hardware';

my $result = $client->advancedSearch($filter_data);

if ($result ->fault) {
    die 'Unable to get the items according to the filters. ' . $result ->faultstring;
}
print Dumper($result ->result);
```
