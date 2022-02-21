---
title: "getTags.php"
description: "getTags.php"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```php
<?php
/**
 * Get all the tags in the account.
 * 
 * The script gets all the tags in the account we make a simple
 * call th the getTags() in the SoftLayer_Account API service
 *
 * Manual pages
 * see http://sldn.softlayer.com/reference/services/SoftLayer_Account
 * see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTags
 * license <http://sldn.softlayer.com/article/License>
 * author SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
require_once ('C:/scripst/getdetails/SoftLayer/SoapClient.class.php');

# Your SoftLayer API key.
# Generate one at https://manage.softlayer.com/Administrative/apiKeychain
$apiUsername = '';
$apiKey = 'apikey_goes_here';

# Declare the API client
$client = Softlayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);

try {
    # Retrieve the tags list.
    $hardware = $client->getTags();
    print_r($hardware);
} catch (Exception $e) {
    die('Unable to list the tags. ' . $e->getMessage());
}

?>
```
