---
title: "search_simple_tag.pl"
description: "search_simple_tag.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_AccountObjectFilter"
tags:
    - "tag"
---


```
# Search VSI by tag
# 
# The script retrieve all the VSIs which contain an
# arbitrary list of tags
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
# 
# License: http://sldn.softlayer.com/article/License
use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use JSON;
use Data::Dumper;

# Your SoftLayer API key and username.
my $username = 'set me';
my $key = 'set me';

# The tag you wish to search
my $tag = "myTag1";

# Creating a SoftLayer API client object
my $account_service = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $username, $key);

# Declaring a filter to search tags
my $filter_name = "SoftLayer_AccountObjectFilter";
my $filter_value = {
    virtualGuests => {
        tagReferences => {
            tag => {
                name => {
                    operation => $tag,
                }
            }
        }
    }
};

$account_service->setHeader($filter_name, $filter_value);

# Sending the request to get the VSIs with the tag
my $result = $account_service->getVirtualGuests();

if ($result->fault) {
    die 'Unable to retrieve the virtual guests. ' . $result->faultstring;
    }
print Dumper($result->result);

```
