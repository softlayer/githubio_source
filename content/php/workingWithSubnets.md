---
title: "Working with Subnets"
description: "A collection of CLI Examples on how to interact with Subnets."
date: "2022-04-22"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Storage"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Account"
tags:
    - "subnet"
    - "networkstorage"
    - "vlan"
---

Read up on the [PHP article](/article/php) for information on how to setup the CLI Framework to get this code to run easily.


## Canceling Image template

This script makes a paginated API call to [SoftLayer_Billing_Item::cancelItem()](/reference/services/SoftLayer_Billing_Item/cancelItem/).

```php
<?php
/**
 * Cancel a Subnet.
 * This script cancels a network subnet using its billing Item.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the services to use
 */
$subnetService ='SoftLayer_Network_Subnet';
$billingItemService = 'SoftLayer_Billing_Item';

$subnetId = 207873;

/**
 * Create a client to the API service.
 */
$subnetClient = SoftLayer_SoapClient::getClient($subnetService, $subnetId, $apiUsername, $apiKey);

try {
    /***
     * Get the Global IP record
     */
    $subnetResult = $subnetClient->getBillingItem();
    $billingItemId = $subnetResult->{'id'};
    print_r($billingItemId);

     try {
        $billingItemClient = SoftLayer_SoapClient::getClient($billingItemService, $billingItemId, $apiUsername, $apiKey);
        $result = $billingItemClient->cancelItem(   False,
                                                    False,
                                                    'No longer needed',
                                                    'Api test');
    print_r($result);

    } catch(Exception $e) {
    echo 'Unable to cancel the Subnet: ' . $e->getMessage();
    }


} catch (Exception $e) {
    echo 'Failed ... Unable to get billing item of Subnet: ' . $e->getMessage();
}

```


## Getting VLAN subnets

This script makes a paginated API call to [SoftLayer_Network_Vlan::getSubnets()](/reference/services/SoftLayer_Network_Vlan/getSubnets/).

```php
<?php
/**
 * Retrieve the subnets for a VLAN
 * 
 * Retrieve all the subnets for a determinate VLAN
 * associated with a SoftLayer customer account
 * We do this with a call to the getSubnets() method in the
 * SoftLayer_Network_Vlan API service. See below for more details.
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets
 * 
 * License: http://sldn.softlayer.com/article/License
 * Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once ('SoftLayer/SoapClient.class.php');

// Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

// The VLAN id you wish to see its subnets
$vlanId = 557984;

// Declaring the API client
$networkVlanService = Softlayer_SoapClient::getClient('SoftLayer_Network_Vlan', null, $apiUsername, $apiKey);

$networkVlanService->setInitParameter($vlanId);

// Sending the request to get the subnets
try {
    $result = $networkVlanService->getSubnets();
    print_r($result);
} catch (Exception $e) {
    die('Unable to retrieve the subnets. ' . $e->getMessage());
}

```


## Listing subnets

This script makes a paginated API call to [SoftLayer_Account::getSubnets()](/reference/services/SoftLayer_Account/getSubnets/).


```php
<?php
/**
 * List Subnets.
 * It retrieves all network subnets associated with an account.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnets
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the service to use
 */
$serviceName ='SoftLayer_Account';

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);

try {

    $receipt = $client->getSubnets();
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to get Subnet list: ' . $e->getMessage();
}

```


## Allowing Access From Subnet

This script makes a paginated API call to [SoftLayer_Network_Storage::allowAccessFromSubnet()](/reference/services/SoftLayer_Network_Storage/allowAccessFromSubnet/).

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


## Creating Subnet

These scripts make a paginated API call to [SoftLayer_Product_Order::verifyOrder()](/reference/services/SoftLayer_Product_Order/verifyOrder/).

### Creating Portable Public Subnet

```php
<?php
/**
 * Create Portable Public Subnet.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the service to use
 */
$serviceName ='SoftLayer_Product_Order';

$priceId =  13980;

/**
 * Set a VLAN to establish where the new IP addresses are routed.
 *
 * @var int
 */
$endPointVlanId = 331044;

/**
 * The number of subnets you wish to order
 *
 * @var int;
 */
$quantity = 1;

// Build a SoftLayer_Container_Product_Order_Network_Subnet object containing
// the order you wish to place. Subnet's don't have a package, so set packageId
// to 0. Since this order is for one item with no sub-options you only have to
// set a single price id in this order.
$orderTemplate = new stdClass();
$orderTemplate->packageId           = 0;
$orderTemplate->prices              = array();
$orderTemplate->prices[0]           = new stdClass();
$orderTemplate->prices[0]->id       = $priceId;
$orderTemplate->endPointVlanId = $endPointVlanId;
$orderTemplate->quantity            = $quantity;


$orderTemplate->itemCategoryQuestionAnswers = array();

// the item category question answers
$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 14;
$itemCategoryQuestionAnswer->answer = '1';  // TOTAL_IPS_IN_30_DAYS
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 15;
$itemCategoryQuestionAnswer->answer = '3';  // # TOTAL_IPS_IN_12_MONTHS
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 16;
$itemCategoryQuestionAnswer->answer = 'Reason for IPs';  // REASON_FOR_IPS
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 9;
$itemCategoryQuestionAnswer->answer = 'Contact Name';  // CONTACT_NAME
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 10;
$itemCategoryQuestionAnswer->answer = 'Contact Job Title';  // # CONTACT_JOB_TITLE
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 11;
$itemCategoryQuestionAnswer->answer = 'contact.email@email.com';  // # CONTACT_EMAIL
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 12;
$itemCategoryQuestionAnswer->answer = '77778727';  // # CONTACT_PHONE_NUMBER
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 313;
$itemCategoryQuestionAnswer->categoryCode = 'sov_sec_ip_addresses_pub';
$itemCategoryQuestionAnswer->questionId = 13;
$itemCategoryQuestionAnswer->answer = true;   // CONTACT_VALIDATED - I agree that the contact information is current and valid.
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);


// Create a SoftLayer API client object to the SoftLayer_Product_Order service.
$client = SoftLayer_SoapClient::getClient
    (
        'SoftLayer_Product_Order',
        null,
        $apiUsername,
        $apiKey
    );

// Place the order for the new subnet.
try {
    // Re-declare the order template as a SOAP variable, so the SoftLayer
    // ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderTemplate,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Network_Subnet',
        'http://api.service.softlayer.com/soap/v3/'
    );

    // verifyOrder() will check your order for errors. Replace this with a call
    // to placeOrder() when you're ready to order. Both calls return a receipt
    // object that you can use for your records.
    //
    // Once your order is placed it'll go through SoftLayer's approval and
    // provisioning process. When it's done you'll have a new
    // SoftLayer_Network_Subnet object ready to use.
    $receipt = $client->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place subnet order: ' . $e->getMessage();
}

```

### Creating Static Public Subnet

```php
<?php
/**
 * Create Static Public Subnet.
 * It orders a new static public subnet
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
 * http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

/**
 * Set the service to use
 */
$serviceName ='SoftLayer_Product_Order';

$priceId = 13983;

/**
 * The id of the IP address that you want to route a static subnet to.
 *
 * @var int
 */
$endPointIpAddressId = 37587549;

/**
 * The number of subnets you wish to order
 *
 * @var int;
 */
$quantity = 1;

// Build a SoftLayer_Container_Product_Order_Network_Subnet object containing
// the order you wish to place. Subnet's don't have a package, so set packageId
// to 0. Since this order is for one item with no sub-options you only have to
// set a single price id in this order.
$orderTemplate = new stdClass();
$orderTemplate->packageId           = 0;
$orderTemplate->prices              = array();
$orderTemplate->prices[0]           = new stdClass();
$orderTemplate->prices[0]->id       = $priceId;
$orderTemplate->endPointIpAddressId = $endPointIpAddressId;
$orderTemplate->quantity            = $quantity;


$orderTemplate->itemCategoryQuestionAnswers = array();

// the item category question answers
$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 53;
$itemCategoryQuestionAnswer->categoryCode = 'static_sec_ip_addresses';
$itemCategoryQuestionAnswer->questionId = 14;
$itemCategoryQuestionAnswer->answer = '1';  // TOTAL_IPS_IN_30_DAYS
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 53;
$itemCategoryQuestionAnswer->categoryCode = 'static_sec_ip_addresses';
$itemCategoryQuestionAnswer->questionId = 15;
$itemCategoryQuestionAnswer->answer = '1';  // TOTAL_IPS_IN_12_MONTHS
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 53;
$itemCategoryQuestionAnswer->categoryCode = 'static_sec_ip_addresses';
$itemCategoryQuestionAnswer->questionId = 9;
$itemCategoryQuestionAnswer->answer = 'ContactJobTitle';  // CONTACT_JOB_TITLE
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 53;
$itemCategoryQuestionAnswer->categoryCode = 'static_sec_ip_addresses';
$itemCategoryQuestionAnswer->questionId = 11;
$itemCategoryQuestionAnswer->answer = 'contact.email@email.com';  // CONTACT_EMAIL
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 53;
$itemCategoryQuestionAnswer->categoryCode = 'static_sec_ip_addresses';
$itemCategoryQuestionAnswer->questionId = 12;
$itemCategoryQuestionAnswer->answer = '77778727';  // CONTACT_PHONE_NUMBER
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;

$itemCategoryQuestionAnswer = new stdClass();
$itemCategoryQuestionAnswer->categoryId = 53;
$itemCategoryQuestionAnswer->categoryCode = 'static_sec_ip_addresses';
$itemCategoryQuestionAnswer->questionId = 13;
$itemCategoryQuestionAnswer->answer = true;   // CONTACT_VALIDATED - I agree that the contact information is current and valid.
$orderTemplate->itemCategoryQuestionAnswers[] = $itemCategoryQuestionAnswer;




/**
 * Create a client to the API service.
 */
$client = SoftLayer_SoapClient::getClient($serviceName, null, $apiUsername, $apiKey);


// Create a SoftLayer API client object to the SoftLayer_Product_Order service.
$client = SoftLayer_SoapClient::getClient
    (
        'SoftLayer_Product_Order',
        null,
        $apiUsername,
        $apiKey
    );

// Place the order for the new subnet.
try {
    // Re-declare the order template as a SOAP variable, so the SoftLayer
    // ordering system knows what type of order you're placing.
    $orderTemplate = new SoapVar
    (
        $orderTemplate,
        SOAP_ENC_OBJECT,
        'SoftLayer_Container_Product_Order_Network_Subnet',
        'http://api.service.softlayer.com/soap/v3/'
    );

    // verifyOrder() will check your order for errors. Replace this with a call
    // to placeOrder() when you're ready to order. Both calls return a receipt
    // object that you can use for your records.
    //
    // Once your order is placed it'll go through SoftLayer's approval and
    // provisioning process. When it's done you'll have a new
    // SoftLayer_Network_Subnet object ready to use.
    $receipt = $client->verifyOrder($orderTemplate);
    print_r($receipt);
} catch (Exception $e) {
    echo 'Unable to place subnet order: ' . $e->getMessage();
}

```
