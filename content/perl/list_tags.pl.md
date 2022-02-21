---
title: "list_tags.pl"
description: "list_tags.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tag"
---


```perl
# List the tags for a VSI
# 
# The script  list all the tags set in an arbitrary  VSI,
# it uses the SoftLayer_Virtual_Guest::getTagReferences method
# to get the tags. For more information please see below
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getTagReferences
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API key and username.
my $username = 'set me';
my $key = 'set me';

# The virtual guest id you wish to get the tags
my $virtual_guest_id = 7844984;

# Creating a SoftLayer API client object
my $virtual_guest_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $username, $key);

$virtual_guest_service->setInitParameter($virtual_guest_id);

# Sending the request to get the tags
my $result = $virtual_guest_service->getTagReferences();

if ($result->fault) {
    die 'Unable to list the tags. ' . $result->faultstring;
}
print Dumper($result->result);

```
