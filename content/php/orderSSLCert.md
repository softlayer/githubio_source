---
title: "Order an SSL Certificate"
description: "Explains how to get the information requried to order an SSL Certificate"
date: "2015-11-11"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Security_Certificate"
    - "SoftLayer_Security_Certificate_Request_ServerType"
tags:
    - "ordering"
    - "ssl"
    - "placeorder"
---

#### Generating a CSR
You will need a csr to make this request, it should be on your local file system. 

```bash
openssl genrsa -out domain.key 2048
openssl req -new -sha256 -key domain.key -out domain.csr
```

```php
<?php

require_once './vendor/autoload.php';
class Example
{
    function __construct() {
        $this->apiUsername = '';
        $this->apiKey = '';
    }

    /*
    * Package 0 is the "Everything else" pacakge, which contains SSL certain. But if you didn't remember that
    * this function will get you that information
    */
    function getAllPackages() {
        $packageClient = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', null, $this->apiUsername, $this->apiKey );
        $packages = $packageClient->getAllObjects();

        print "ID -> Name \n";
        foreach($packages as $package) {
            print $package->id . " -> " . $package->name . "\n";
        }
    }

    /*
    * Each package has a lot of items, so this function will show you all of those along with their prices. 
    * Search through it for the proper SSL item you want to order, and take note of its price
    */
    function getPackageById($id=0, $onlyShow=0) {
        $packageClient = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', $id, $this->apiUsername, $this->apiKey );
        $package = $packageClient->getItems();
        print "ID, KeyName, Description \n";
        foreach ($package as $item) {
            if ($onlyShow == 0 || $onlyShow == $item->id) {
                print $item->id . " , " . $item->keyName . " , " . $item->description . "\n" ;
                print_r($item->prices); 
            }
        }
    }


    /*
    * Change verifyOrder to placeOrder when you are actually ready to make a certificate 
    */
    function placeOrder($csrFilename='./domain.csr') {

        $csr = file_get_contents($csrFilename);
        $client = \SoftLayer\XmlRpcClient::getClient('SoftLayer_Product_Order', null, $this->apiUsername, $this->apiKey );
        $order = new stdClass();

        $addressInfo = new stdClass();
        $addressInfo->address = new stdClass();
        $addressInfo->address->addressLine1 = "1234 fleet street";
        $addressInfo->address->city = "Houston";
        $addressInfo->address->countryCode = "US";
        $addressInfo->address->postalCode =  "77002";
        $addressInfo->address->state = "TX";
        $addressInfo->emailAddress ="chgallo@lablayer.info";
        $addressInfo->firstName = "Christopher";
        $addressInfo->lastName = "Gallo";
        $addressInfo->organizationName = "SoftLayer";
        $addressInfo->phoneNumber = "281-123-4567";
        $addressInfo->title = "Dev"; 

        $price = new stdClass();
        $price->id = 1836;

        $container = new stdClass();
        $container->complexType = "SoftLayer_Container_Product_Order_Security_Certificate";
        $container->packageId = 0;
        $container->quantity = 1;
        $container->serverCount = 1;
        $container->serverType = 'apacheapachessl';
        $container->prices = array($price);
        $container->certificateSigningRequest = $csr;

        $container->technicalContact = $addressInfo;
        $container->administrativeContact = $addressInfo;
        $container->organizationInformation = $addressInfo;
        $container->billingContact = $addressInfo;
        # Needs to be a VERY specific email @ the domain you are registering
        # admin / administrator / hostmaster / root / webmaster / mailmaster
        $container->orderApproverEmailAddress = "admin@lablayer.info";  

        $order->orderContainers = array();
        $order->orderContainers[0] = $container;
        // print_r($order);
        $result = $client->verifyOrder($order);
        print_r($result);
    }

    /*
    * This info is required for the serverType property. 
    */
    function getServerTypes() {
        // http://sldn.softlayer.com/reference/services/SoftLayer_Security_Certificate_Request_ServerType
        $client = \SoftLayer\SoapClient::getClient('SoftLayer_Security_Certificate_Request_ServerType', null, $this->apiUsername, $this->apiKey );
        $types = $client->getAllObjects();
        print_r($types);
    }

}


$example = new Example();
// Figure out which package has the SSL certs
$example->getAllPackages();

// Package 0, item 964 is the ssl cert we want to see the prices for.
$example->getPackageById(0, 964 );

// 964 , SSL_CERTIFICATE_RAPIDSSL_1_YEAR , RapidSSL - 1 year
// [id] => 1836
// [setupFee] => 19

$example->getServerTypes();
/*
[1] => stdClass Object
    (
        [description] => Apache + ApacheSSL
        [id] => 2
        [name] => apacheapachessl
        [value] => 22
    )
*/
$example->placeOrder();    
```

