---
title: "get_tags.pl"
description: "get_tags.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```
# Get all the tags in the account.
#
# The script gets all the tags in the account. We make a simple
# call the getTags() in the SoftLayer_Account API service.
# 
# Important Manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTags
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;
use strict;
 
# Your SoftLayer API username and key.
my $api_username = 'set me';
my $api_key = 'set me';

# Declaring the service
my $account_service = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key);

# Getting the tags  
my $result = $account_service->getTags(); 
 
# If there was an error returned from the SoftLayer API then die out with the
# error message.
if ($result->fault) {
    die "Unable to set the user metadata." . $result->faultstring;
}

print Dumper($result->result);

```
