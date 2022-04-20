---
title: "Working with Image Templates"
description: "A collection of CLI Examples on how to interact with Image Templates."
date: "2022-04-20"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Account"
tags:
    - "image-templates"
    - "imagetemplates"
---

Read up on the [Perl article](/article/perl) for information on how to setup the CLI Framework to get this code to run easily.


## Deleting an image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject/).


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

## Getting image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::getObject()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject).


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

## Listing Image templates

This script makes a paginated API call to [SoftLayer_Account::getPrivateBlockDeviceTemplateGroups()](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups/).


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

## Sharing image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::permitSharingAccess()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess/).


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

## Unsharing image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::denySharingAccess()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess/).


```perl
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

## Creating flex image templates

### Creating flex image template from a virtual guest

This script makes a paginated API call to [SoftLayer_Virtual_Guest::captureImage()](/reference/services/SoftLayer_Virtual_Guest/captureImage/).


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

### Creating flex image template from a server 

This script makes a paginated API call to [SoftLayer_Hardware_Server::captureImage()](/reference/services/SoftLayer_Hardware_Server/captureImage/).


```perl
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

### Creating standard image template

This example contains deprecated methods or syntax and needs to be updated. Please use caution when using. This script makes a paginated API call to [SoftLayer_Virtual_Guest::createArchiveTransaction()](/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction/).


```perl
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
