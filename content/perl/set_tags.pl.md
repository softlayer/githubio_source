---
title: "set_tags.pl"
description: "set_tags.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tag"
---


```
# Set tags for a VSI
#
# The script sets the tags for an arbitrary VSI,
# it makes a single call to the SoftLayer_Virtual_Guest::setTags method
# For more information please see below.
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setTags
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API key and username.
my $username = 'set me';
my $key = 'set me';

# The virtual guest id you wish to set the tags
my $virtual_guest_id = 7844984;

# The tags you wish to set in the VSI
my $tags = "mytag1,mytag2,mytag3";

# Creating a SoftLayer API client object
my $virtual_guest_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $username, $key);

$virtual_guest_service->setInitParameter($virtual_guest_id);

# Sending the request to set the tags
my $result = $virtual_guest_service->setTags($tags);

if ($result->fault) {
    die 'Unable to set the tags. ' . $result->faultstring;
}
print Dumper($result->result);

```
