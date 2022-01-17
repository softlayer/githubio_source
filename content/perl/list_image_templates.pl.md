---
title: "list_image_templates.pl"
description: "list_image_templates.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```perl
# Get private image template
# 
# The script calls the SoftLayer_Account::getPrivateBlockDeviceTemplateGroups method
# to list the private templates in the account and uses an object mask
# to display more related information of the images templates
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups
# http://sldn.softlayer.com/reference/dataypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Creating a SoftLayer API client object
my $account_service = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $username, $key);

# Declaring an object mask to get more information about the images templates
my $object_mask = "mask[summary,note,status[name],storageRepository[datacenter],transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter],blockDevices[diskImage[type]]]]";

# Setting the object Mask
$account_service->setObjectMask($object_mask);
# Setting the object mask in the service and call the getPrivateBlockDeviceTemplateGroups to list the image templates
my $result = $account_service->getPrivateBlockDeviceTemplateGroups();
if ($result->fault) {
    die 'Unable to get the image templates. ' . $result->faultstring;
}
print Dumper($result->result);

```
