---
title: "get_the_details_image_template.pl"
description: "get_the_details_image_template.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```perl
# Get image template details.
# 
# The script gets more details of an arbitrary image template,
# it uses an object mask to retrieve the information.
# For more information please see below.
# 
# Import manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The image template which you wish more details
my $image_template_id = 171272;

# Creating a SoftLayer API client object
my $block_device_template_group_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest_Block_Device_Template_Group', undef, $username, $key);

# Declaring an object mask to get more information about the images templates
my $object_mask = "mask[summary,note,status[name],storageRepository[datacenter],transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter],blockDevices[diskImage[type]]]]";

# Setting the object Mask
$block_device_template_group_service->setObjectMask($object_mask);
# Setting the init Parameter
$block_device_template_group_service->setInitParameter($image_template_id);
# Setting the object mask in the service and call the getPrivateBlockDeviceTemplateGroups to list the image templates
my $result = $block_device_template_group_service->getObject();
if ($result->fault) {
    die 'Unable to get the images templates. ' . $result->faultstring;
}
print Dumper($result->result);

```
