---
title: "delete_image_template.pl"
description: "delete_image_template.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```perl
# Delete an image template
# 
# The script makes a single call to the SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject
# method to delete an image template. For more information see below.
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The image template which you wish to delete
my $image_template_id = 171272;

# Creating a SoftLayer API client object
my $block_device_template_group_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest_Block_Device_Template_Group', undef, $username, $key);

# Setting the init Parameter
$block_device_template_group_service->setInitParameter($image_template_id);

# Calling the delete object method
my $result = $block_device_template_group_service->deleteObject();
if ($result->fault) {
    die 'Unable to delete the image template. ' . $result->faultstring;
}
print Dumper($result->result);

```
