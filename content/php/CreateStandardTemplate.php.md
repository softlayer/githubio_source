---
title: "CreateStandardTemplate.php"
description: "CreateStandardTemplate.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Virtual_Guest_Block_Device"
tags:
    - "imagetemplates"
---


```
<?php
/**
 * Create standard image template.
 *
 * The example creates a standard image template from a CCI
 * which contains 3 disk. for more information see below.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createArchiveTransaction
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
 *
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('Softlayer/SoapClient.class.php');

$username = 'set me';
$key = 'set me';
$endPoint = "set me";

/**
 * Building a skeleton SoftLayer_Virtual_Guest_Block_Device object
 * containing the disk which will be in the image template
 * It is not necesary to specify all disks in the virtual server
 * only is required specify the first disk.
 * To get the list of block devices in the Virtual Guest
 * call the SoftLayer_Virtual_Guest::getBlockDevices method
*/
$idBlockDevices = array
(
    8020158, 9196790, 9289828
);

$blockDevices = array();
 
foreach ($idBlockDevices as $id){
    $blockDevice = new stdClass();
    $blockDevice->id = $id;
    $blockDevices[] = $blockDevice;
}

$groupName = "the name for the template";
$note = "an optional note";

/**
 * The virtual guest Id of the virtual server from you want
 * to take the image template.
 * To get a list of all your virtual servers in your account
 * use the Softlayer::getVirtualGuests method
*/ 
$virtualGuestId = 6143038;

$virtualGuestService = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $username, $key, $endPoint);

# Setting the init parameter
$virtualGuestService->setInitParameter($virtualGuestId);

# Calling the captureImage method along with our captureTemplate to create the flexImage
$result = $virtualGuestService->createArchiveTransaction($groupName, $blockDevices, $note);
print_r($result);

?>

```
