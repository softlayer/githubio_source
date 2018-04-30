---
title: "retrieve_metadata.pl"
description: "retrieve_metadata.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```
#
# Retrieve the user data for the VSIs in the account
# 
# The script gets the user metadata for a VSI in the account. We make a simple
# call the getVirtualGuests() in the SoftLayer_Virtual_Guest API service
# and we set an object mask to get the information about the user data
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
# 
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;
use strict;
 
# Your SoftLayer API username and key
my $api_username = 'set me';
my $api_key = 'set me';

# Declaring the service
my $account_service = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key);

# Adding the object mask to the call to get the information about the user data.
my $object_mask = 'mask[userData]';
$account_service->setObjectMask($object_mask);

# Retrieving our account's VSIs records.
my $servers = $account_service->getVirtualGuests();
 
# If there was an error returned from the SoftLayer API then die out with the
# error message.
if ($servers->fault) {
    die "Unable to retrieve the VSI list. " . $servers->faultstring;
}

print Dumper($servers->result);

```
