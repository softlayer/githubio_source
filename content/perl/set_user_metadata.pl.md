---
title: "set_user_metadata.pl"
description: "set_user_metadata.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "metadata"
---


```
# Set the user data for a VSI.
# 
# The script sets the user metadata for a VSI we make a simple
# call the setUserMetadata() in the SoftLayer_Virtual_Guest API service
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setUserMetadata
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;
use strict;
 
# Your SoftLayer API username and key.
my $apiUsername = 'set me';
my $apiKey = 'set me';

# The user data you wish to set
my $user_data = ["this is my user data perl"];

# The id of the VSI where you want to set the user data
my $virtual_guest_id = 7370502;

# Declaring the service
my $virtual_guest_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $apiUsername, $apiKey);

# Setting the init parameter in the service
$virtual_guest_service->setInitParameter($virtual_guest_id);

# Setting the user data  
my $result = $virtual_guest_service->setUserMetadata($user_data); 
 
# If there was an error returned from the SoftLayer API then die out with the
# error message.
if ($result->fault) {
    die "Unable to set the user metadata." . $result->faultstring;
}

print Dumper($result->result);

```
