---
title: "list_bare_metals.pl"
description: "list_bare_metals.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```perl
# List Bare Metal servers.
#
# The script retrieves a list of all bare metal servers in your
# account. it makes a single call to the Softlayer_Account::getHardware
# method for more information see below.
#
# Important manual pages:
# https://sldn.softlayer.com/reference/services/SoftLayer_Account
# https://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
# https://sldn.softlayer.com/reference/datatype/SoftLayer_Hardware/
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username.
my $username = 'set me';

# Your SoftLayer API key.
my $key = 'set me';

# Creating a SoftLayer API client object
my $client = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $username, $key);

# We will retrieve the additional information
# for each server:
# primaryIpAddress
# primaryBackendIpAddress
# datacenter
# datacenterName
# serviceProvider
# hardwareFunctionDescription
my $object_mask = {
    'hardware' => {
        'primaryIpAddress' => {},
        'primaryBackendIpAddress' => {},
        'datacenter' => {},
        'datacenterName' => {},
        'serviceProvider' => {},
        'hardwareFunctionDescription' => {},
   }
};

$client->setObjectMask($object_mask);

# getHardware() will get all the bare metal servers that an account has.
my $hardware_list = $client->getHardware();

if ($hardware_list -> fault) {
    die 'Unable to list the servers. ' . $hardware_list->faultstring;
}

# Pretty print the Bare metal list
print Dumper($hardware_list->result);

```
