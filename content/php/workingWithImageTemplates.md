---
title: "Working with Image Templates"
description: "A collection of CLI Examples on how to interact with Image Templates."
date: "2022-04-21"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Account"
tags:
    - "imagetemplates"
---

Read up on the [PHP article](/article/php) for information on how to setup the CLI Framework to get this code to run easily.


## Deleting Image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject/).

```php
<?php
/**
 * Delete an image template
 *
 * Important pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# The image template which you wish to delete
$imageTemplateId = 171272;

# Creating a SoftLayer API client object
$blockDeviceTemplateGroupService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest_Block_Device_Template_Group', null, $username, $key);

# Setting the init Parameter
$blockDeviceTemplateGroupService->setInitParameter($imageTemplateId);

# Calling the delete object method
$result = $blockDeviceTemplateGroupService->deleteObject();
print_r($result);

?>

```


## Getting an Image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::getObject()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject/).

```php
<?php
/**
 * Get more details about the images templates
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# The image template which you wish more details
$imageTemplateId = 171272;

# Declaring an object mask to get more information about the images templates
$objectMask = "mask[summary,note,status[name],storageRepository[datacenter],transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter],blockDevices[diskImage[type]]]]";

# Creating a SoftLayer API client object
$blockDeviceTemplateGroupService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest_Block_Device_Template_Group', null, $username, $key);

# Setting the object Mask
$blockDeviceTemplateGroupService->setObjectMask($objectMask);

# Setting the init Parameter
$blockDeviceTemplateGroupService->setInitParameter($imageTemplateId);

# Setting the object mask in the service and call the getPrivateBlockDeviceTemplateGroups to list the image template
$result = $blockDeviceTemplateGroupService->getObject();
print_r($result);
?>

```


## Listing Image templates

This script makes a paginated API call to [SoftLayer_Account::getPrivateBlockDeviceTemplateGroups()](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups/).

```php
<?php
/**
 * List all the private image templates in the account
 * 
 * The script calls the SoftLayer_Account::getPrivateBlockDeviceTemplateGroups method
 * to list the private templates in the account and uses an object mask
 * to display more related information of the images templates
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * 
*/
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# Creating a SoftLayer API client object
$accountService = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $username, $key);

# Declaring an object mask to get more information about the images templates
$objectMask = "mask[summary,note,status[name],storageRepository[datacenter],transaction[transactionGroup,transactionStatus],children[storageRepository[datacenter],blockDevices[diskImage[type]]]]";

# Setting the object Mask
$accountService->setObjectMask($objectMask);

# Setting the object mask in the service and call the getPrivateBlockDeviceTemplateGroups to list the image templates
$result = $accountService->getPrivateBlockDeviceTemplateGroups();
print_r($result);
?>

```


## Sharing an Image Template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::permitSharingAccess()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess/).

```php
<?php
/**
 * Share an image template to another Softlayer account
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# The image template which you wish to share
# to get the list of images templates in your account call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
$imageTemplateId = 315894;

# The account you wish to share the image template
$accountToShare = 207819;

# Creating a SoftLayer API client object
$blockDeviceTemplateGroupService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest_Block_Device_Template_Group', null, $username, $key);

# Setting the init Parameter
$blockDeviceTemplateGroupService->setInitParameter($imageTemplateId);

$result = $blockDeviceTemplateGroupService->permitSharingAccess($accountToShare);
print_r($result);

?>
```


## Unsharing an Image Template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::denySharingAccess()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess/).

```php
<?php
/**
 * Unshare an image template
 *  
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * 
*/
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# The image template which you wish to unshare
# To get the list of images templates in your account call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
$imageTemplateId = 315894;

# The account you wish to unshare the image template
$accountToShare = 207819;

# Creating a SoftLayer API client object
$blockDeviceTemplateGroupService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest_Block_Device_Template_Group', null, $username, $key);

# Setting the init Parameter
$blockDeviceTemplateGroupService->setInitParameter($imageTemplateId);

# Calling the denySharingAccess method to ushare the image template
$result = $blockDeviceTemplateGroupService->denySharingAccess($accountToShare);
print_r($result);

?>
```


## Creating Image Templates

### Creating flex image from a Server

This script makes a paginated API call to [SoftLayer_Hardware_Server::captureImage()](/reference/services/SoftLayer_Hardware_Server/captureImage/).

```php
<?php
/**
 * Create an flex image from a Server
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template
 * http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/captureImage
 * http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# The virtual guest Id of the machine you wish to create the image template
$hardwareServerId = 7438972;

# Creating an SoftLayer_Container_Disk_Image_Capture_Template Skeleton
# wich contains the information for our flex image
$captureTemplate = new stdClass();
    $captureTemplate->description = "test";
    $captureTemplate->name = "reloadFlexImage";
    $captureTemplate->summary = "test summary";

$captureTemplate = new SoapVar
    (
        $captureTemplate,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Disk_Image_Capture_Template',
        'http://api.service.softlayer.com/soap/v3/'
    );

# Creating a SoftLayer API client object
$hardwareServerService = SoftLayer_SoapClient::getClient('SoftLayer_Hardware_Server', null, $username, $key);

# Setting the init parameter
$hardwareServerService->setInitParameter($hardwareServerId);

# Creating the standard image template from the desiere CCI
$result = $hardwareServerService->captureImage($captureTemplate);
print_r($result);

?>
```

### Creating flex image from a CCI

This example contains deprecated methods or syntax and needs to be updated. Please use caution when using. This script makes a paginated API call to [SoftLayer_Virtual_Guest::createArchiveTransaction()](/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction/).

```php
<?php
/**
 * Example to create an flex image from a CCI
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/captureImage
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
 * 
 * License <http://sldn.softlayer.com/wiki/index.php/license>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$username = 'set me';
$key = 'set me';

# The virtual guest id of the machine you wish to create the image template
$virtualGuestId = 7438972;

# Creating an SoftLayer_Container_Disk_Image_Capture_Template Skeleton
# wich contains the information for our flex image
$captureTemplate = new stdClass();
    $captureTemplate->description = "test";
    $captureTemplate->name = "reloadFlexImage";
    $captureTemplate->summary = "test summary";

$captureTemplate = new SoapVar
    (
        $captureTemplate,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Disk_Image_Capture_Template',
        'http://api.service.softlayer.com/soap/v3/'
    );

# Creating a SoftLayer API client object
$virtualGuestService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $username, $key);

# Setting the init parameter
$virtualGuestService->setInitParameter($virtualGuestId);

# Creating the standard image template from the desiere CCI
$result = $virtualGuestService->createArchiveTransaction($captureTemplate);
print_r($result);

?>
```
