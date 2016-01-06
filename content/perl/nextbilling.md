---
title: "Retrieve the amount of your next invoice"
description: "Returns the amount in USD of the next invoice using getNextInvoiceTotalAmount"
date: "2016-01-06"
classes: ["SoftLayer_Account"]
tags:
  - "invoice"
  - "billing"
---

```perl
use lib "./softlayer-api-perl-client/";
use SoftLayer::API::SOAP;
use Data::Dumper;

my $api_username = "x";
my $api_key = "a";
my $client = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key);


my $result;
$result = $client->getNextInvoiceTotalAmount();
print "Next Invoice Total: " . $result->result . "\$\n" ;
```
