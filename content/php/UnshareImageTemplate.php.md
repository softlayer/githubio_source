---
title: "UnshareImageTemplate.php"
description: "UnshareImageTemplate.php"
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
