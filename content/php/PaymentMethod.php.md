---
title: "PaymentMethod.php"
description: "PaymentMethod.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Payment_Card_ManualPayment"
    - "SoftLayer_Account"
    - "SoftLayer_Locale_Country"
    - "SoftLayer_Billing_Payment_Card_ChangeRequest"
tags:
    - "payment"
---


```php
<?php
/**
 * This script retrieves the record data associated with the submission of a Credit Card Change Request. 
 * If the onlyChangeNicknameFlag parameter is set to true, the nickname of the credit card will be changed 
 * immediately without requiring approval by an agent. 
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/requestCreditCardChange
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Payment_Card_ChangeRequest
 *
 * @license <http://sldn.softlayer.com/wiki/index.php/license>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */
require_once __DIR__.'/vendor/autoload.php';

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
 * Declare parameters for the request to credit card change
 * @var $vatid string - EU member states VAT ID.
 * @var $paymentRoleName string - keyName of the card's payment role
 * @var $onlyChangeNicknameFlag boolean - 
 */
 $vatid = "";
 $paymentRoleName = "";
 $onlyChangeNicknameFlag = "";

/**
 * Setting values for Billing Address
 * You can use address on file, setting the "$useCompanyInformationOnFile" value as "true". 
 * If the value is "false", you need to fill all the values bellow it
 */
$useCompanyInformationOnFile = false;
// Fill these values if you set "$useCompanyInformationOnFile" as false
$companyName = "newCompany";
$firstName = "Jhon";
$lastName = "Travolta";
$streetAddress = "Av. opsss";
$country = "Bolivia";
$state = "Cochabamba";
$city = "Cochabamba";
$postalCode = "656284325";
$email = "noreply@softlayer.com";
$phone = "7888665598";

/**
 * Setting values for Payment Information
 */
$cardNickname = "set me";
$cardNumber = "set me";
$expirationMonth = "set me";
$expirationYear = "set me";
$securityCode = "set me";

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Locale_Country" service
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$countryService = \SoftLayer\SoapClient::getClient('SoftLayer_Locale_Country', null, $username, $apiKey);

// Declare an object mask to get states from countries
$objectMask = "mask[states]";
$countryService -> setObjectMask($objectMask);

/**
 * Build a SoftLayer_Billing_Payment_Card_ManualPayment object with details required to request a manual payment
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Payment_Card_ManualPayment
 */
 $request = new stdClass();
 $request -> billingNameCompany = $companyName;
 $request -> billingNameFirst = $firstName;
 $request -> billingNameLast = $lastName;
 $request -> billingAddressLine1 = $streetAddress;
 $request -> billingCountryCode = $country;
 $request -> billingState = $state;
 $request -> billingCity = $city;
 $request -> billingPostalCode = $postalCode;
 $request -> billingEmail = $email;
 $request -> billingPhoneVoice = $phone;
 
 $request -> cardNickname = $cardNickname;
 $request -> cardAccountNumber = $cardNumber;
 $request -> cardExpirationMonth = $expirationMonth;
 $request -> cardExpirationYear = $expirationYear;
 $request -> creditCardVerificationNumber = $securityCode;
  
 // Declare a flag to validate the request
 $requestFlag = false;
 
try {
	// Verifying if "Use Company Information on File" is enabled ($useCompanyInformationOnFile as true)
	if($useCompanyInformationOnFile)
	{
		$account = $accountService -> getObject();
		
		$request -> billingNameCompany = $account -> companyName;
 		$request -> billingNameFirst = $account -> firstName;
 		$request -> billingNameLast = $account -> lastName;
 		$request -> billingAddressLine1 = $account -> address1;
		if(isset($account -> address2))
		{$request -> billingAddressLine2 = $account -> address2;}
 		$request -> billingCountryCode = $account -> country;
 		$request -> billingState = $account -> state;
 		$request -> billingCity = $account -> city;
 		$request -> billingPostalCode = $account -> postalCode;
 		$request -> billingEmail = $account -> email;
 		$request -> billingPhoneVoice = $account -> officePhone;
		$requestFlag = true;
	}
	else{
		// Get Countries
		$countries = $countryService -> getAvailableCountries();
		// Verifying Country and State to get shorName from them
		foreach($countries as $countryObj)
		{
			if($countryObj -> longName == $country)
			{
				$request -> billingCountryCode = $countryObj -> shortName;
				if(sizeof($countryObj -> states)>0)
				{
					if($state != "")
					{
						foreach($countryObj -> states as $stateObj)
						{
							if(strpos($stateObj -> longName, $state) !== false)
							{
								$request -> billingState = $stateObj -> shortName;
								$requestFlag = true;
								break;
							}
						}
						if($requestFlag == false)
						{
							print_r("The state that you specified is not valid or doesn't exist.");
						}
					}
					else{print_r("You need to specified a value in '\$state'");}
				}
				else{
					$request -> billingState = "OT";
					$requestFlag = true;
				}
			}
		}
	}
	// If country and state are valid, we proceed to send the request
	if($requestFlag)
	{
		$result = $accountService -> requestCreditCardChange($request, $vatid, $paymentRoleName, $onlyChangeNicknameFlag);
		print_r($result);
	}

} catch(Exception $e) {
	echo "Unable to submit a credit card change request: " . $e -> getMessage();
}

```
