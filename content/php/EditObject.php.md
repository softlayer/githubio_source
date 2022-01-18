---
title: "EditObject.php"
description: "EditObject.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_SoapClient"
tags:
    - "virtualguest"
---


```php
<?php
/**
 * Edit Virtual Guest
 *
 * This script edits a Virtual Guest's properties
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/editObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once "C:/Php/SoftLayer/SoftLayer/SoapClient.class.php";

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
 * Declare Id from Virtual Guest to be edit
 * @var int
 */
 $vsiId = 8170116;

// Create a SoftLayer API client object for "SoftLayer_Virtual_Guest" services
$virtualGuestService = SoftLayer_SoapClient::getClient("SoftLayer_Virtual_Guest", null, $username, $apiKey);

// Build a skeleton SoftLayer_Virtual_Guest object with the properties defined that you wish to change.
$templateObject = new stdClass();
$templateObject -> hostname = "rcv3-test";
$templateObject -> domain = "rcv.com";
$templateObject -> notes = "This is for test";

// Set up init parameter
$virtualGuestService -> setInitParameter($vsiId);

try {
    $result = $virtualGuestService -> editObject($templateObject);
    print_r("Virtual Guest: " . $vsiId . " edited?: ". $result);
} catch(Exception $e) {
    echo "Unable to edit Virtual Guest: " . $e -> getMessage();
}

```
