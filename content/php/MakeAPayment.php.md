---
title: "MakeAPayment.php"
description: "MakeAPayment.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Payment_Card_ManualPayment"
    - "SoftLayer_Account"
    - "SoftLayer_Locale_Country"
tags:
    - "payment"
---


```php
<?php
/**
 * This script submits a request for manual payment. This kind of request are permitted at minimum amount of $2.00. 
 * Customer may submit a Credit Card Payment (Mastercard, Visa, American Express or a PayPal payment).
 *
 * Important manual pages:
 * @see http://sldn.softlayer.com/reference/services/SoftLayer_Account/requestManualPayment
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Payment_Card_ManualPayment 
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

// Create a SoftLayer API client object to the "SoftLayer_Account" and "SoftLayer_Locale_Country" service
$accountService = \SoftLayer\SoapClient::getClient('SoftLayer_Account', null, $username, $apiKey);
$countryService = \SoftLayer\SoapClient::getClient('SoftLayer_Locale_Country', null, $username, $apiKey);

/**
 * Setting values for Payment Details
 */
$amount = 109;

/**
 * Setting values for Credit Card Details
 */
$nameOnCardFirst = "set me";
$nameOnCardLast = "set me";
$cardNumber = "set me";
$expirationMonth = "set me";
$expirationYear = "set me";
$securityCode = "set me";

/**
 * Setting values for Billing Address
 * You can use address on file, setting the "$billingAddressFlag" value as "true". 
 * If the value is "false", you need to fill all the values bellow it
 */
$billingAddressFlag = false;
// Fill these values if you set "$billingAddressFlag" as false
$streetAddress = "Av. Melchor Perez de Olguin";
$streetAddressOptional = "";
$city = "Dallas";
$emailAddress = "noreply@softlayer.com";
// Specify the whole name for Country and State. e.g. Country: Canada - State: Quebec
$country = "United States";
$state = "Michigan";
$postalCode = "234234445";
$phoneNumber = "7088995584";

// Declare an object mask to get states from countries
$objectMask = "mask[states]";
$countryService -> setObjectMask($objectMask);

/**
 * Build a SoftLayer_Billing_Payment_Card_ManualPayment object with details required to request a manual payment
 * @see http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Payment_Card_ManualPayment
 */
 $request = new stdClass();
 $request -> amount = $amount;
 $request -> billingAddressLine1 = $streetAddress;
 $request -> billingAddressLine2 = $streetAddressOptional;
 $request -> billingCity = $city;
 $request -> billingCountryCode = $country;
 $request -> billingEmail = $emailAddress;
 $request -> billingNameFirst = $nameOnCardFirst;
 $request -> billingNameLast = $nameOnCardLast;
 $request -> billingPhoneVoice = $phoneNumber;
 $request -> billingPostalCode = $postalCode;
 $request -> billingState = $state;
 $request -> cardAccountNumber = $cardNumber;
 $request -> cardExpirationMonth = $expirationMonth;
 $request -> cardExpirationYear = $expirationYear;
 $request -> creditCardVerificationNumber = $securityCode;
  
 // Declare a flag to validate the request
 $requestFlag = false;
 
try {
	
	// Verifying if "Use Address on File" is enabled ($billingAddressFlag as true)
	if($billingAddressFlag)
	{
		$account = $accountService -> getObject();
		$request -> billingAddressLine1 = $account -> address1;
		if(isset($account -> address2))
		{$request -> billingAddressLine2 = $account -> address2;}
		$request -> billingCity = $account -> city;
		$request -> billingCountryCode = $account -> country;
		$request -> billingEmail = $account -> email;
		$request -> billingState = $account -> state;
		$request -> billingPostalCode = $account -> postalCode;
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
		$result = $accountService -> requestManualPayment($request);
		print_r($result);
	}

} catch(Exception $e) {
	echo "Unable to submit a request for manual payment: " . $e -> getMessage();
}

```
