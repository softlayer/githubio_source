---
title: "create_flex_image.pl"
description: "create_flex_image.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Disk_Image_Capture_Template"
tags:
    - "imagetemplates"
---


```perl
# Create an flex image from a Server
# 
# The script makes a single call to the SoftLayer_Hardware_Server::captureTemplate
# method in order to create a flex image from the bare metal server.
# For more information please see below.
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/captureImage
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>

use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The virtual guest id of the machine you wish to create the image template
my $virtual_guest_id = 7438972;

# Creating an SoftLayer_Container_Disk_Image_Capture_Template Skeleton
# wich contains the information for our flex image
my $capture_template = bless({
    "description" => "test",
    "name" => "reloadFlexImage",
    "summary" => "test summary",
}, 'slapi:SoftLayer_Container_Disk_Image_Capture_Template');

# Creating a SoftLayer API client object
my $virtual_guest_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $username, $key);

# Setting the init parameter
$virtual_guest_service->setInitParameter($virtual_guest_id);

# Calling the captureImage method along with our captureTemplate to create the flexImage
my $result = $virtual_guest_service->captureImage($capture_template);
if ($result->fault) {
    die 'Unable to create the flex image. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The flex image has been created succesfully. ");

```
