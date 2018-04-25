---
title: "AddPersonRecord.php"
description: "AddPersonRecord.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
    - "SoftLayer_Account_Regional_Registry_Detail"
    - "SoftLayer_SoapClient"
tags:
    - "rirregistration"
---


```
<?php
/**
 * Add Person Record
 *
 * This script adds person record using: SoftLayer_Account_Regional_Registry_Detail::createObject
 * method. Person Record is used for RIR Registration.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account_Regional_Registry_Detail/createObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property
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
 * Define Person Record information
 * @var string $organization
 * @var string $firstName
 * @var string $lastName
 * @var string $streetAddress
 * @var string $city
 * @var string $country
 * @var string $zipCode
 * @var string $email
 * @var string $abuseEmail
 * @var string $phoneNumber
 */
$organization = "Organization testRcv2";
$firstName = "First name test";
$lastName = "Last name test";
$streetAddress = "Street address test";
$city = "Cochabamba";
$country = "Bolivia";
$zipCode = "591";
$email = "noreply@softlayer.com";
$abuseEmail = "noreply@softlayer.com";
$phoneNumber = "987654321";

// Create a SoftLayer API client object to the "SoftLayer_Account_Regional_Registry_Detail" service
$client = SoftLayer_SoapClient::getClient("SoftLayer_Account_Regional_Registry_Detail", null, $username, $apiKey);

// Build array for SoftLayer_Account_Regional_Registry_Detail_Property
$properties = array( array("propertyTypeId" => 61, "value" => $organization, "sequencePosition" => 0), array("propertyTypeId" => 11, "value" => $email, "sequencePosition" => 0), array("propertyTypeId" => 2, "value" => $firstName, "sequencePosition" => 0), array("propertyTypeId" => 3, "value" => $lastName, "sequencePosition" => 0), array("propertyTypeId" => 4, "value" => $streetAddress, "sequencePosition" => 0), array("propertyTypeId" => 5, "value" => $city, "sequencePosition" => 0), array("propertyTypeId" => 6, "value" => "OT", "sequencePosition" => 0), array("propertyTypeId" => 7, "value" => $zipCode, "sequencePosition" => 0), array("propertyTypeId" => 8, "value" => $country, "sequencePosition" => 0), array("propertyTypeId" => 14, "value" => $abuseEmail, "sequencePosition" => 0), array("propertyTypeId" => 9, "value" => $phoneNumber, "sequencePosition" => 0), );

// Build SoftLayer_Account_Regional_Registry_Detail object to add new Person Record
$templateObject = new stdClass();
$templateObject -> detailTypeId = 3;
$templateObject -> properties = $properties;

try {
    // Try to add new Person Record
    $receipt = $client -> createObject($templateObject);
    print_r($receipt);
} catch(Exception $e) {

    echo "Unable to add person record: " . $e -> getMessage();
}

```
