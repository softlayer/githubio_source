---
title: "CreateObject.php"
description: "CreateObject.php"
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
 * Create Virtual Guest
 *
 * This script creates a Virtual Guest on an account using the alternative simplified for it.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

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
 * Build SoftLayer_Virtual_Guest skeleton to create a Virtual Server. To verify the current available options,
 * try the following method: SoftLayer_Virtual_Guest::getCreateObjectOptions.
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions
 */
$templateObject = new stdClass();
$templateObject -> hostname = "ad-test";
$templateObject -> domain = "softlayer.com";
$templateObject -> startCpus = 1;
$templateObject -> maxMemory = 1024;
$templateObject -> hourlyBillingFlag = True;
$templateObject -> localDiskFlag = True;
$templateObject -> operatingSystemReferenceCode = "CENTOS_LATEST";
// Define Data center
$templateObject -> datacenter = new stdClass();
$templateObject -> datacenter -> name = "ams01";

// Create a SoftLayer API client object for "SoftLayer_Virtual_Guest" services
$virtualGuestService = SoftLayer_SoapClient::getClient("SoftLayer_Virtual_Guest", null, $username, $apiKey);

try {
    $result = $virtualGuestService -> createObject($templateObject);
    print_r($result);
} catch(Exception $e) {
    echo "Unable to create Virtual Guest: " . $e -> getMessage();
}

```
