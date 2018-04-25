---
title: "get_server_cost.pl"
description: "get_server_cost.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "billing"
---


```
# Get the recurring cost of all servers on your account.
# 
# Get a list of servers on a SoftLayer account along with their recurring
# monthly costs. We can get that by calling getHardware() in the
# SoftLayer_Account API service with an object mask to retrieve cost.
# 
# Important manual pages
# see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# see http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getCost
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

# Declaring the service
my $account_service = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key);

# Declaring the object mask to get information about cost of the bare metal server
my $object_mask = 'mask(SoftLayer_Hardware_Server).cost';
$account_service->setObjectMask($object_mask);

my $servers = $account_service->getHardware();
 
# If there was an error returned from the SoftLayer API then die out with the
# error message.
if ($servers->fault) {
    die "Unable to retrieve the bare metal servers." . $servers->faultstring;
}

print Dumper($servers->result);

```
