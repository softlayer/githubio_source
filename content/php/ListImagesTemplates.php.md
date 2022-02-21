---
title: "ListImagesTemplates.php"
description: "ListImagesTemplates.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_SoapClient"
tags:
    - "imagetemplates"
---


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
