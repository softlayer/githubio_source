---
title: "get_resource_records.pl"
description: "get_resource_records.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain_resource_record"
---


```perl
# Get Resource Records.
# This script retrieves the individual records contained within a domain record.
#
# Important manual pages:
# @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
#
# @license <http://sldn.softlayer.com/article/License>
# @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib '/path/to/SoftLayer/';
use Data::Dumper;
use SoftLayer::API::SOAP;
use strict;

# Set your SoftLayer API username and key.
my $api_username = 'set me';
my $api_key = 'set me';

# Set the domain id to get the related records
my $dns_id = 1880851;

# Service to use to get the records.
my $domain_service ='SoftLayer_Dns_Domain';
					
# Create a Domain client to the API service.
my $domain_client = SoftLayer::API::SOAP->new($domain_service, $dns_id, $api_username, $api_key);

my $result = $domain_client->getResourceRecords();
				   
if ($result->fault) {
	die 'There is an error when trying to get the resource records...' . $result->faultstring;
} else {
	print Dumper($result);
}

```
