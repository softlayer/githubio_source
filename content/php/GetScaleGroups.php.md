---
title: "GetScaleGroups.php"
description: "GetScaleGroups.php"
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
 * Get Scale Groups
 * 
 * This script retrieves all scale groups on this account. This make a call to SoftLayer_Account::getScaleGroups method.
 * 
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getScaleGroups
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group
 * 
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com> 
 */
require_once "C:/PhpSoftLayer/SoftLayer/SoftLayer/SoapClient.class.php";

// Your SoftLayer API username.
$username = "set me";

// Your SoftLayer API key.
$apiKey = "set me";

// Create a SoftLayer API client object for "SoftLayer_Account" service
$account = SoftLayer_SoapClient::getClient("SoftLayer_Account", null, $username, $apiKey);

// Define an objectMask to retrieve status and regionalGroup information from scale groups
$account -> setObjectMask("mask[status[name], regionalGroup[name]]");
	
	try {
		$scaleGroups  = $account -> getScaleGroups();
		for ($i=0; $i < sizeof($scaleGroups); $i++)
		{
			print_r(($i+1) . " Id: " . $scaleGroups[$i] -> id . "   Name: " . $scaleGroups[$i] -> name . "    Status: " . $scaleGroups[$i] -> status -> name .
			"     Region: " . $scaleGroups[$i] -> regionalGroup -> name . "\n");
		}
	} catch(Exception $e)
	{
		echo "Unable to retrieve Scale Groups" . $e -> getMessage();
	}

?>
```
