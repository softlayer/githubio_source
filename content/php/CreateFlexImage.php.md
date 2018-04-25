---
title: "CreateFlexImage.php"
description: "CreateFlexImage.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Container_Disk_Image_Capture_Template"
tags:
    - "imagetemplates"
---


```
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
