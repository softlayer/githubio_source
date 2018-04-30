---
title: "edit_resource_record.pl"
description: "edit_resource_record.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns_domain_resource_record"
---


```
# Edit Resource Records.
# This script edits an existing domain resource record.
#
# Important manual pages:
# @see http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject
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

# Set the resource id that you want to edit.
# To get resource record ids, please use: SoftLayer_Dns_Domain::getResourceRecords
my $resource_id = 59843492;

# Service to use to create a new record.
my $resource_record_service ='SoftLayer_Dns_Domain_ResourceRecord';

# Set a new TTL value to edit. The valid values to edit are:
#          900 (15 Min)
#          3600 (1 Hour)
#          86400 (1 Day)
#          604800 (1 Week)
my $new_ttl = 900;

# Creating a template to configure our resource record edition.
my $object_template = {
						'data'=> '127.4.0.1',
						'host'=> '@',
						'ttl'=>  $new_ttl
					};
						
# Create a Resource record client to the API service.
my $resource_record_client = SoftLayer::API::SOAP->new($resource_record_service, $resource_id, $api_username, $api_key);

my $result = $resource_record_client->editObject($object_template);
				   
if ($result->fault) {
			die 'There is an error when trying to edit the resource record...' . $result->faultstring;
} else {
			print Dumper($result);

}

```
