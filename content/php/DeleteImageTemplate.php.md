---
title: "DeleteImageTemplate.php"
description: "DeleteImageTemplate.php"
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
