---
title: "DeleteScaleGroup.php"
description: "DeleteScaleGroup.php"
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
 * Delete Scale Group
 *
 * This script deletes a scale group. This can only be done on an empty and active group.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/deleteObject
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getScaleGroups
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
 * The Scale Group name that you wish to delete.
 * They are displayed in the following link: https://control.softlayer.com/autoscale
 * @var string
 */
$groupName = "set me with Scale Group name";

// Create a SoftLayer API client object for "SoftLayer_Account" and "SoftLayer_Scale_Group" services
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);
$client = SoftLayer_SoapClient::getClient("SoftLayer_Scale_Group", null, $username, $apiKey);

// Define an objectFilter to filter the scale group by name
$filter = new stdClass();
$filter -> scaleGroups = new stdClass();
$filter -> scaleGroups -> name = new stdClass();
$filter -> scaleGroups -> name -> operation = "_=" . $groupName;
$account -> setObjectFilter($filter);


try {
	// Get Scale Groups 
	$result = $account -> getScaleGroups();
    
	// Set init parameter, to delete the scale group
	$client -> setInitParameter($result[0] -> id);
    
	/**
	 * It is possible to delete a group and destroy all members of it.
	 * The following method can help with it:
	 * SoftLayer_Scale_Group::forceDeleteGroup method.
	 * The Scale Group must be active or suspended to delete.
	 * 
	 * Review the following link to get more information:
	 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/forceDeleteObject
	 * 
	 * e.g.
	 * $result = $client -> forceDeleteObject();  
	 */
	$result = $client -> forceDeleteObject();
	print_r("Scale Group " . $groupName . " was deleted?: " . $result);
} catch(Exception $e) {
	echo "Unable to delete Scale Group " . $e -> getMessage();
}

?>
```
