---
title: "unshare_image_template.pl"
description: "unshare_image_template.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```
# Un-share an image template
#
# The script un-shares an image template it makes a call to  SoftLayer_Virtual_Guest_Block_Device_Template_Group::denySharingAccess
# method for more information please see below:
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess
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

# The image template which you wish to unshare
# To get the list of images templates in your account call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
my $image_template_id = 315894;

# The account you wish to unshare the image template
my $account_to_share = 207819;

# Creating a SoftLayer API client object
my $block_device_template_group_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest_Block_Device_Template_Group', undef, $username, $key);

# Setting the init Parameter
$block_device_template_group_service->setInitParameter($image_template_id);
# Calling the denySharingAccess method to ushare the image template
my $result = $block_device_template_group_service->denySharingAccess($account_to_share);
if ($result->fault) {
    die 'Unable to unshare the image template. ' . $result->faultstring;
}
print Dumper($result->result);

```
