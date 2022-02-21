---
title: "EditScaleGroup.php"
description: "EditScaleGroup.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Scale_Group"
    - "SoftLayer_SoapClient"
tags:
    - "scalegroup"
---


```php
<?php
/**
 * Edit Scale Group
 *
 * This script edits scale group. The name, minimumMemberCount and maximumMemberCount fields  can be edited at any time.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/editObject
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
 * The Scale Group name that you wish to edit
 * They are displayed in the following link: https://control.softlayer.com/autoscale
 * @var string
 */
$groupName = "set me with Auto Scale Group name";

/**
 * Build a SoftLayer_Scale_Group object with properties that you want to edit
 * 
 * @var int $cooldown - The number of seconds this group will wait after lastActionDate before performing another action
 * @var int $maximumMemberCount - The greatest number of virtual guest members that are allowed on this group
 * @var int $minimumMemberCount - The fewest number of virtual guest members that are allowed on this group
 * @var string $name - The name of this scale group. It must be unique on the account.
 */
$cooldown = 84;
$name = "set me with new name";
$maximumMemberCount = 27;
$minimumMemberCount = 2;

// Create a SoftLayer API client object for "SoftLayer_Account" and "SoftLayer_Scale_Group" services
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$client = SoftLayer_SoapClient::getClient("SoftLayer_Scale_Group", null, $username, $apiKey);

// Define an objectFilter to filter the scale group by name
$filter = new stdClass();
$filter -> scaleGroups = new stdClass();
$filter -> scaleGroups -> name = new stdClass();
$filter -> scaleGroups -> name -> operation = "_=" . $groupName;
$account -> setObjectFilter($filter);

// It is possible to edit a member configuration from scale group, you can edit the following template
$virtualTemplate = new stdClass();
$virtualTemplate -> hourlyBillingFlag = True;
$virtualTemplate -> hostname = "hosname";
$virtualTemplate -> domain = "softlayer.com";
$virtualTemplate -> startCpus = 4;
$virtualTemplate -> maxMemory = 2048;
$virtualTemplate -> localDiskFlag = false;
$virtualTemplate -> operatingSystemReferenceCode = "UBUNTU_LATEST";
$virtualTemplate -> privateNetworkOnlyFlag = false;

// Build a SoftLayer_Scale_Group template which will be used for edit.  
$scaleGroup = new stdClass();
$scaleGroup -> cooldown = $cooldown;
$scaleGroup -> maximumMemberCount = $maximumMemberCount;
$scaleGroup -> minimumMemberCount = $minimumMemberCount;
$scaleGroup -> name = $name;
$scaleGroup -> virtualGuestMemberTemplate = $virtualTemplate;

try {
    // Get Scale Groups 
    $result = $account -> getScaleGroups();

    // Set init parameter, to edit scale group
    $client -> setInitParameter($result[0] -> id);

    $result = $client -> editObject($scaleGroup);
	print_r("Scale Group " . $groupName . " was edited?: " . $result);
} catch(Exception $e) {
    echo "Unable to edit Scale Group" . $e -> getMessage();
}

?>
```
