---
title: "share_image_template.pl"
description: "share_image_template.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```perl
# Share image template.
#
# The script shares an image template to another account, it makes
# a single call to SoftLayer_Virtual_Guest_Block_Device_Template_Group::permitSharingAccess
# method.
# For more information please see below.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess
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

# The image template which you wish to share
# To get the list of images templates in your account call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
my $image_template_id = 315894;

# The account you wish to share the image template
my $account_to_share = 207819;

# Creating a SoftLayer API client object
my $block_device_template_group_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest_Block_Device_Template_Group', undef, $username, $key);

# Setting the init Parameter
$block_device_template_group_service->setInitParameter($image_template_id);

# Calling the delete object method
my $result = $block_device_template_group_service->permitSharingAccess($account_to_share);
if ($result->fault) {
    die 'Unable to share the image template. ' . $result->faultstring;
}
print Dumper($result->result);

```
