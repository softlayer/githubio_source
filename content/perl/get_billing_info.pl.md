---
title: "get_billing_info.pl"
description: "get_billing_info.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Info"
    - "SoftLayer_Account"
tags:
    - "billing"
---


```perl
# Retrieve the billing info for the Bare Metals in the account.
#
# This script makes a single call to the getHardware() method in the
# SoftLayer_Account API service and uses an object mask to get the
# billing info for each Bare Metal server in the account.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Info
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use JSON;
use Data::Dumper;
use strict;

# Your SoftLayer API username and key.
my $api_username = 'set me';
my $api_key = 'set me';

# Declaring the API client
my $account_service = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key);

# Declaring the object mask to get information about the billing item.
my $object_mask = 'mask[id, hostname, domain, datacenter[longName], billingItem[recurringFee]]';
$account_service->setObjectMask($object_mask);

my $servers = $account_service->getHardware();

# If there was an error returned from the SoftLayer API then die out with the
# error message.
if ($servers->fault) {
    die "Unable to retrieve the bare metal servers." . $servers->faultstring;
}

print Dumper($servers->result);

```
