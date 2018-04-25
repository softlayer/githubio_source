---
title: "GetRegionalGroups.php"
description: "GetRegionalGroups.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location_Group_Regional"
    - "SoftLayer_SoapClient"
tags:
    - "scalegroup"
---


```
<?php
/**
 * Get Regional Groups
 *
 * This script gets all regional groups which are useful to set regionalGroupId at the moment to create a Scale Group.
 * 
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Regional/getAllObjects
 * 
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com> 
 */
require_once "C:/PhpSoftLayer/SoftLayer/SoftLayer/SoapClient.class.php";

// Your SoftLayer API username.
$username = "set me";

// Your SoftLayer API key.
$apiKey = "set me";

// Create a SoftLayer API client object for "SoftLayer_Location_Group_Regional" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Location_Group_Regional", null, $username, $apiKey);

	try {
		$regionalGroups = $client -> getAllObjects();
		for ($i=0; $i < sizeof($regionalGroups); $i++)
		{
			print_r(($i+1) . " Id: " . $regionalGroups[$i] -> id . "   Name: " . $regionalGroups[$i] -> name . "    Description: " . $regionalGroups[$i] -> description . "\n");
		}
	} catch(Exception $e)
	{
		echo "Unable to retrieve Regional Groups" . $e -> getMessage();
	}

?>
```
