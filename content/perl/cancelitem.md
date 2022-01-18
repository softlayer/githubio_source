---
title: "Cancel item"
description: "Invoke cancelService to cancel an item by Billing ID"
date: "2016-01-06"
classes: ["SoftLayer_Billing_Item"]
tags:
  - "cancelservice"
  - "billing"
---

```perl
#!/usr/bin/perl
use lib "/path/to/softlayer-api-perl-client/";
use SoftLayer::API::SOAP;
use Data::Dumper;

my $api_username = "a";
my $api_key = "x";

#Canel service
# https://api.softlayer.com/rest/v3/SoftLayer_Billing_Item/<BILLING_ID>/cancelService
my $billing_id = $result->result->{'id'};
my $billing_client = SoftLayer::API::SOAP->new('SoftLayer_Billing_Item', $billing_id, $api_username, $api_key);
$result = $billing_client->cancelService();
print Dumper($result->result);
```
