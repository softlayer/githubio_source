---
title: "get_invoices.pl"
description: "get_invoices.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "billing"
---


```
# Retrieve the invoice information.
#
# This script makes a single call to the getInvoices() method in the
# SoftLayer_Account API service and uses an object mask to get more
# information about the invoices.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
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
my $object_mask = 'mask[payment,amount,invoiceTotalOneTimeAmount,invoiceTotalRecurringAmount,invoiceTotalOneTimeTaxAmount,invoiceTotalRecurringTaxAmount]';
$account_service->setObjectMask($object_mask);

# Retrieving the invoices for the account.
my $servers = $account_service->getInvoices();

# If there was an error returned from the SoftLayer API then die out with the
# error message.
if ($servers->fault) {
    die "Unable to retrieve the invoices." . $servers->faultstring;
}

print Dumper($servers->result);

```
