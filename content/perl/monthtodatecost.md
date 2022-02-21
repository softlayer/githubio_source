---
title: "Retrieve the month to date cost of an hourly VSI"
description: "Returns the month to date cost of an hourly VSI using getBillingItem and Object Masks"
date: "2016-01-06"
classes: ["SoftLayer_Virtual_Guest"]
tags:
  - "objectmask"
  - "billing"
  - "getbillingitem"
---

```perl
#!/usr/bin/perl
use lib "/path/to/softlayer-api-perl-client/";
use SoftLayer::API::SOAP;
use Data::Dumper;

my $api_username = "x";
my $api_key = "a";
my $client = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key);

# SoftLayer_Virtual_Guest/<VSI_ID>/getBillingItem?objectMask=mask\[createDate,hoursUsed,hourlyRecurringFee,currentHourlyCharge\]"
# CHANGE ME to the id of the virtual guest you want to check
my $virtual_guest_id = 12345678;
my $virtual_guest = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', $virtual_guest_id, $api_username, $api_key);
my $objectMask = {
    'createDate' => '',
    'hoursUsed' => '',
    'hourlyRecurringFee' => '',
    'currentHourlyCharge' => ''
};

$result = $virtual_guest->getBillingItem();
my $cost;
$cost = $result->result->{'hoursUsed'} * $result->result->{'hourlyRecurringFee'};
print $result->result->{'hoursUsed'} . " hours @ " . $result->result->{'hourlyRecurringFee'} . "\$/hour = " . $cost . " \$\n";
```

Example Response:
```
1 hours @ .045$/hour = 0.045 $
```
