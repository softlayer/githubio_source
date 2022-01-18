---
title: "SearchTags.php"
description: "SearchTags.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "tag"
---


```php
<?php

/**
 * Search VSI by tag
 * 
 * The script retrieve all the VSIs which contain an
 * arbitrary list of tags
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('Softlayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

$accountService = Softlayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);

// List of tags to look for
$tags = array("tag1", "tag2");

// Declaring an object filter to get only the virtual servers which contains the tags that we are looking for
$filter = new stdClass();
$filter->virtualGuests = new stdClass();
$filter->virtualGuests->tagReferences = new stdClass();
$filter->virtualGuests->tagReferences->tag = new stdClass();
$filter->virtualGuests->tagReferences->tag->name = new stdClass();
$filter->virtualGuests->tagReferences->tag->name->operation = new stdClass();
$filter->virtualGuests->tagReferences->tag->name->operation = "in";
$filter->virtualGuests->tagReferences->tag->name->options = array();
$filter->virtualGuests->tagReferences->tag->name->options[0] = new stdClass();
$filter->virtualGuests->tagReferences->tag->name->options[0]->name = "data";
$filter->virtualGuests->tagReferences->tag->name->options[0]->value = $tags;

$accountService->setObjectFilter($filter);

try {
    // Sending the request to get the virtual guest using the filter
    $result = $accountService->getVirtualGuests();
    print_r($result);

} catch (Exception $e) {
    echo 'Unable to search the tags : ' . $e -> getMessage();
}

?>
```
