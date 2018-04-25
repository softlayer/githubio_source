---
title: "edit_details.pl"
description: "edit_details.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
#
# Edit a bare metal server's basic information
#
# Changing the notes property for a single bare metal server record to the sentence "This
# is my fastest server!" using the editObject() method in the
# SoftLayer_Hardware_Server API service. See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/editObject
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The name of the server we wish to edit.
my $server_name = 'set me';

# Declaring a new API service object for the SoftLayer_Account API service.
my $client = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $username, $key);

# Calling the getHardware() method from the SoftLayer_Account API service to get
# a list of hardware on your account, including id numbers.
my $hardware_list = $client->getHardware();

# If there was an error returned from the SoftLayer API then bomb out with the
# error message.
if ($hardware_list->fault) {
    die 'Unable to list the servers. ' . $hardware_list->faultstring;
}

# Define the new local properties to set.
#
# A SoftLayer_Hardware_Server record has a few local properties that you can
# change via the API. Every service's editObject() method takes a single
# parameter, a skeleton object that only defines the properties we wish to
# change. While we're only editing a server's notes in this example you can
# also use editObject() to edit the server's hostname and domain record.
my $edit_template = {
    'notes' => 'This is my fastest server!'
};

my $hardware_id = '';

# Looking for the server name to get its id
$hardware_records = $hardware_list->result;
for my $i (0 .. $#{$hardware_records}) {
    my $hardware = $hardware_records->[$i];
    if ($hardware->{hostname} eq $server_name) {
        $hardware_id = $hardware->{id}
    }
}

# If the server name was not found we throw an error message.
if ($hardware_id eq ''){
    die 'Unable to find the server with the name '. $server_name;
}

# Declaring a new API service object for the SoftLayer_Hardware_Server API service.
$client = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);

# Setting the init parameter with the server Id
$client->setInitParameter($hardware_id);

# Editing our server record.
my $result = $client->editObject($edit_template);

# If there was an error returned from the SoftLayer API then bomb out with the
# error message.
if ($result->fault) {
    die 'Unable to edit the servers. ' . $result->faultstring;
}

print ('Server edited');

```
