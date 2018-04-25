---
title: "CreateScaleGroup.php"
description: "CreateScaleGroup.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location_Group_Regional"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroup"
---


```
<?php
/**
 * Create Scale Group
 *
 * This script creates a scale group. The minimumMemberCount is greater than zero or desiredMemberCount
 * is present, guest members will be created right away.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/createObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once "C:/PhpSoftLayer/SoftLayer/SoftLayer/SoapClient.class.php";

/**
 * Your SoftLayer API username
 * @var string
 */
$username = "set me";

/**
 * Your SoftLayer API key
 * Generate one at: https://control.softlayer.com/account/users
 * @var string
 */
$apiKey = "set me";

/**
 * Build SoftLayer_Scale_Group object that you wish to create.
 * 
 * @var int $cooldown - The amount of seconds this group will wait after lastActionDate before performing another action
 * @var int $maximumMemberCount - The maximun number of virtual guest members that are allowed on this group
 * @var int $minimumMemberCount - The fewest number of virtual guest members that are allowed on this group
 * @var string $name - The name of this scale group. It must be unique on the account.
 * @var int $regionalGroupId - The identifier of the regional group this scaling group is assigned to.
 * @var int $terminationPolicyId - The termination policy for the group. 
 */
$cooldown = 20;
$maximumMemberCount = 20;
$minimumMemberCount = 0;
$name = "ScaleGroupName";
$regionalGroupId = 102; // to retrieve them, try: SoftLayer_Location_Group_Regional::getAllObjects e.g. 102 - as-hkg-central-1
$terminationPolicyId = 2;

// Create a SoftLayer API client object for "SoftLayer_Scale_Group" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Scale_Group", null, $username, $apiKey);

// The datacenter that a virtual guest resides in
$location = new stdClass();
$location -> name = "hkg02";

/**
 * Define a template to create guest members with. This is the same template accepted by 
 * SoftLayer_Virtual_Guest::createObject method. The hostname provided will have an arbitrary value appended to 
 * it for each guest created. Also, hourlyBillingFlag cannot be false. The datacenter is provided it must be in 
 * the region of this group. Vlans cannot be provided for the template, it will use vlans provided to this group instead.
 * 
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 */
$virtualTemplate = new stdClass();
$virtualTemplate -> hourlyBillingFlag = True;
$virtualTemplate -> hostname = "test";
$virtualTemplate -> domain = "softlayer.local";
$virtualTemplate -> startCpus = 1;
$virtualTemplate -> maxMemory = 1024;
$virtualTemplate -> localDiskFlag = false;
$virtualTemplate -> datacenter = $location;
$virtualTemplate -> operatingSystemReferenceCode = "UBUNTU_LATEST";
$virtualTemplate -> privateNetworkOnlyFlag = false;

// Build a SoftLayer_Scale_Group template
$group = new stdClass();
$group -> cooldown = $cooldown;
$group -> maximumMemberCount = $maximumMemberCount;
$group -> minimumMemberCount = $minimumMemberCount;
$group -> name = $name;
$group -> regionalGroupId = $regionalGroupId;
$group -> terminationPolicyId = $terminationPolicyId;
$group -> suspendedFlag = false;
$group -> virtualGuestMemberTemplate = $virtualTemplate;

try {
    $scaleGroups = $client -> createObject($group);
    print_r($scaleGroups);

} catch(Exception $e) {
    echo "Unable to create Scale Group" . $e -> getMessage();
}

?>

```
