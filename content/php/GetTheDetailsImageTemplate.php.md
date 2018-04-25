---
title: "GetTheDetailsImageTemplate.php"
description: "GetTheDetailsImageTemplate.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "imagetemplates"
---


```
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
