---
title: "AllowAccessFromSubnet.php"
description: "AllowAccessFromSubnet.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Storage"
tags:
    - "networkstorage"
---


```php
<?php
/**
 * Allow Access From Subnet. It is only allowed for File Network Storages.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/allowAccessFromSubnet
 * @see http://sldn.softlayer.com/article/Object-Masks
 * @see http://sldn.softlayer.com/article/Object-Filters
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once dirname(__FILE__) . "/SoftLayer/SoapClient.class.php";

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

// Create a SoftLayer API client object to the "SoftLayer_Network_Storage" service
$storageService = SoftLayer_SoapClient::getClient("SoftLayer_Network_Storage", null, $username, $apiKey);

// Setting init parameters
$storageService -> setInitParameter(4494879);

// Build a SoftLayer_Network_Subnet object
$subnet = new stdClass();
$subnet -> id = 400241;

try {
    $receipt = $storageService -> allowAccessFromSubnet($subnet);
    print_r($receipt);

} catch(Exception $e) {
    echo "Unable to allow access from Subnet:  " . $e -> getMessage();
}

```
