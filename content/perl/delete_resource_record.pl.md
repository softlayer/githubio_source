---
title: "delete_resource_record.pl"
description: "delete_resource_record.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain_resource_record"
---


```perl
# Delete Resource Record.
# This script deletes a domain's resource record.
#
# Important manual pages:
# @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject
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

# Set the id of item to delete
# To get resource record ids, please use: SoftLayer_Dns_Domain::getResourceRecords
my $record_id = 59845680;

# Service to use to create a new record.
my $resource_record_service ='SoftLayer_Dns_Domain_ResourceRecord';

					
# Create a Resource record client to the API service.
my $resource_record_client = SoftLayer::API::SOAP->new($resource_record_service, $record_id, $api_username, $api_key);

my $result = $resource_record_client->deleteObject();
				   
if ($result->fault) {
	die 'There is an error when trying to delete the resource record...' . $result->faultstring;
} else {
	print Dumper($result);
}

```
