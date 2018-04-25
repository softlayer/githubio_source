---
title: "create_image_template_standard.pl"
description: "create_image_template_standard.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Block_Device"
tags:
    - "imagetemplates"
---


```
# Create standard image template.
#
# The example creates a standard image template from a CCI
# which contains 3 disk. for more information see below.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';
my $end_point = 'set me';

# Building a skeleton SoftLayer_Virtual_Guest_Block_Device object
# containing the disk which will be in the image template
# It is not neccesary to specify all disks in the virtual server
# only is required specify the firts disk.
# To get the list of block devices in the Virtual Guest
# call the SoftLayer_Virtual_Guest::getBlockDevices method
my $block_devices_template = [
    {
        "id" => 8020158
    },
    
    {
        "id" => 9196790
    },
    
    {
        "id" => 9289828
    }
];

my $group_name = "the name for the template";
my $note = "an optional note";

# The virtual guest id of the virtual server from you want
# to take the image template.
# To get a list of all your virtual servers in your account
# use the Softlayer::getVirtualGuests method 
my $virtual_guest_id = 6143038;

# Creating a SoftLayer API client object
my $virtual_guest_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $username, $key, $end_point);

# Setting the init parameter
$virtual_guest_service->setInitParameter($virtual_guest_id);

# Creating the standard image template from the desiere CCI
my $result = $virtual_guest_service->createArchiveTransaction($group_name, $block_devices_template, $note);
if ($result->fault) {
    die 'Unable to create image template. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The image template was created successfully");

```
