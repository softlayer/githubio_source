---
title: "add_resource_record.pl"
description: "add_resource_record.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain_resource_record"
---


```
# Create Resource Record.
# This script creates a new domain resource record.
#
# Important manual pages:
# @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
#      http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject
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

# Set the domain id that you want to add a new record.
my $dns_id = 1880851;

# Service to use to create a new record.
my $resource_record_service ='SoftLayer_Dns_Domain_ResourceRecord';

# Creating a template to configure our DNS Zone edition.
my $object_template = {
						'domainId'=>  $dns_id,
						'data'=> '127.1.1.1',
						'host'=> '@',
						'type'=> 'a'
					};
						
# Create a Resource record client to the API service.
my $resource_record_client = SoftLayer::API::SOAP->new($resource_record_service, undef, $api_username, $api_key);

my $result = $resource_record_client->createObject($object_template);
				   
if ($result->fault) {
			die 'There is an error when trying to add a new resource record...' . $result->faultstring;
} else {
			print Dumper($result);
}

```
