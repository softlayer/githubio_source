---
title: "EditPersonRecord.php"
description: "EditPersonRecord.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_SoapClient"
    - "SoftLayer_Account_Regional_Registry_Detail"
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
tags:
    - "rirregistration"
---


```
<?php
/**
 * Edit Person Record
 *
 * This script edits an existing person record using: SoftLayer_Account_Regional_Registry_Detail::editObject
 * method.
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account_Regional_Registry_Detail/editObject
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail
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
 * Define Id of Account Regional Registry Detail(Person Record) to edit
 * @var int
 */
$registryId = 467201;

/**
 * Define "Person Record" information to be edited
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
$organization = "Organization hoioo";
$firstName = "First name test2";
$lastName = "Last name test2";
$streetAddress = "Street address test2";
$city = "Cochabamba2";
$country = "Bolivia";
$zipCode = "592";
$email = "noreply2@softlayer.com";
$abuseEmail = "noreply2@softlayer.com";
$phoneNumber = "2222222222";

// Create a SoftLayer API client object for "SoftLayer_Account_Regional_Registry_Detail" service
$regionalRegistryService = SoftLayer_SoapClient::getClient("SoftLayer_Account_Regional_Registry_Detail", null, $username, $apiKey);

// Build array for SoftLayer_Account_Regional_Registry_Detail_Property
$properties = array( array("propertyTypeId" => 61, "value" => $organization, "sequencePosition" => 0), array("propertyTypeId" => 11, "value" => $email, "sequencePosition" => 0), array("propertyTypeId" => 2, "value" => $firstName, "sequencePosition" => 0), array("propertyTypeId" => 3, "value" => $lastName, "sequencePosition" => 0), array("propertyTypeId" => 4, "value" => $streetAddress, "sequencePosition" => 0), array("propertyTypeId" => 5, "value" => $city, "sequencePosition" => 0), array("propertyTypeId" => 6, "value" => "OT", "sequencePosition" => 0), array("propertyTypeId" => 7, "value" => $zipCode, "sequencePosition" => 0), array("propertyTypeId" => 8, "value" => $country, "sequencePosition" => 0), array("propertyTypeId" => 14, "value" => $abuseEmail, "sequencePosition" => 0), array("propertyTypeId" => 9, "value" => $phoneNumber, "sequencePosition" => 0), );

// Setting init parameter of "Person Record" to be edited
$regionalRegistryService -> setInitParameter($registryId);

// A skeleton SoftLayer_Account_Regional_Registry_Detail object with only properties to be edited.
$templateObject = new stdClass();
$templateObject -> detailTypeId = 3;
$templateObject -> properties = $properties;

// Define Object Mask to get Properties property
$regionalRegistryService -> setObjectMask("mask[properties]");

try {
    $result = $regionalRegistryService -> editObject($templateObject);
    echo "Person Record edited?: " . $result . "\n";
} catch(Exception $e) {
    echo "Unable to edit person record: " . $e -> getMessage();
}

```
