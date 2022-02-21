---
title: "GetBillingInfo.php"
description: "GetBillingInfo.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Info"
    - "SoftLayer_Account"
tags:
    - "billing"
---


```php
<?php
/**
* Retrieve the billing info for the Bare Metals in the account.
*
* This script makes a single call to the getHardware() method in the
* SoftLayer_Account API service and uses a object mask to get the
* billing info for each Bare Metal server in the account.
*
* Important manual pages
* http://sldn.softlayer.com/reference/services/SoftLayer_Account
* http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
* http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Info
*
* License: http:'sldn.softlayer.com/article/License
* Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
**/
require_once ('C:/scripst/getdetails/SoftLayer/SoapClient.class.php');

# Client configuration
# Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

# Declaring the API client
$accountService = Softlayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);

# Declaring the object mask to get information about the billing item.
$objectMask = 'mask[id, hostname, domain, datacenter[longName], billingItem[recurringFee]]';
$accountService->setObjectMask($objectMask);

try {
    # Retrieving the bare metal servers for the account.
    $servers = $accountService->getHardware();
    print_r($servers);
} catch (Exception $e) {
    die('Unable to retrieve the bare metal servers. ' . $e->getMessage());
}

?>

```
