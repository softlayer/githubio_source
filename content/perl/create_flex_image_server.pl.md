---
title: "create_flex_image_server.pl"
description: "create_flex_image_server.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Disk_Image_Capture_Template"
tags:
    - "imagetemplates"
---


```
# Create an flex image from a Server
# 
# The script makes a single call to the SoftLayer_Hardware_Server::captureTemplate
# method in order to create a flex image from the bare metal server.
# For more information please see below.
# 
# Important manual page:
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

# The virtual guest Id of the machine you wish to create the image template
my $hardware_server_id = 7438972;

# Creating an SoftLayer_Container_Disk_Image_Capture_Template Skeleton
# wich contains the information for our flex image
my $capture_template = bless({
    "description" => "test",
    "name" => "reloadFlexImage",
    "summary" => "test summary",
}, 'slapi:SoftLayer_Container_Disk_Image_Capture_Template');

# Creating a SoftLayer API client object
my $hardware_server_service = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);

# Setting the init parameter
$hardware_server_service->setInitParameter($hardware_server_id);

# Calling the captureImage method along with our captureTemplate to create the flexImage
my $result = $hardware_server_service->captureImage($capture_template);
if ($result->fault) {
    die 'Unable to create the flex image. ' . $result->faultstring;
}
print Dumper($result->result);
print ("The flex image has been created succesfully. ");

```
