---
title: "Order Server with security software"
description: "An example of how to include add-on software to a server order"
date: "2015-11-11"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
tags:
    - "ordering"
    - "server"
    - "mc-afee"
    - "security"
---


```php
<?php

require_once './vendor/autoload.php';

class Example
{
    function __construct() {
        $this->apiUsername = '';
        $this->apiKey = '';
    }

    function getAllPackages() {
        $packageClient = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', null, $this->apiUsername, $this->apiKey );
        $packages = $packageClient->getAllObjects();

        print "ID -> Name \n";
        foreach($packages as $package) {
            print $package->id . " -> " . $package->name . "\n";
        }
    }


    function getPackageById($id=0, $onlyShow=0, $showPrices = 1) {
        $packageClient = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', $id, $this->apiUsername, $this->apiKey );
        $package = $packageClient->getItems();
        print "ID, KeyName, Description \n";
        foreach ($package as $item) {
            if ($onlyShow == 0 || $onlyShow == $item->id) {
                print $item->id . " , " . $item->keyName . " , " . $item->description . "\n" ;
                if ($showPrices) {
                    print_r($item->prices); 
                }
            }
        }
    }

    function getActiveRamItems($packageId = 0) {
        $client = \SoftLayer\XmlRpcClient::getClient('SoftLayer_Product_Package', $packageId, $this->apiUsername, $this->apiKey );
        $items = $client->getActiveRamItems();
        print_r($items);
    }

    function getActiveServerItems($packageId = 0) {
        $client = \SoftLayer\XmlRpcClient::getClient('SoftLayer_Product_Package', $packageId, $this->apiUsername, $this->apiKey );
        $items = $client->getActiveServerItems();
        print_r($items);
    }



    function placeOrder() {

        $client = \SoftLayer\XmlRpcClient::getClient('SoftLayer_Product_Order', null, $this->apiUsername, $this->apiKey );
        $order = new stdClass();
        $container = new stdClass();

        $priceArray = array(
            49485, //INTEL_XEON_2650_2_00
            36253, //OS_WINDOWS_2012_R2_FULL_DC_64_BIT_2         
            49405, //RAM_16_GB
            876, //DISK_CONTROLLER_NONRAID
            49759, //HARD_DRIVE_1_00_TB_SATA_2
            49759, //HARD_DRIVE_1_00_TB_SATA_2
            274, //1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS
            50261, //BANDWIDTH_20000_GB
            21, //1_IP_ADDRESS
            906, //REBOOT_KVM_OVER_IP
            420, //UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT
            56, //MONITORING_HOST_PING_AND_TCP_SERVICE
            57, //NOTIFICATION_EMAIL_AND_TICKET
            58, // response, AUTOMATED_NOTIFICATION
            418, //NESSUS_VULNERABILITY_ASSESSMENT_REPORTING
            413, //MCAFEE_HOST_INTRUSION_PROTECTION_WREPORTING
            594, //MCAFEE_VIRUSSCAN_ANTIVIRUS_WINDOWS                    
        );
        $container->prices = array();
        foreach ($priceArray as $item) {
            $priceId = new stdClass();
            $priceId->id = $item;
            $container->prices[] = $priceId;
        }

        $container->complexType = "SoftLayer_Container_Product_Order_Hardware_Server";
        $container->packageId = 273;
        $container->quantity = 1;
        $container->location = 448994;  //DAL05
        $container->serverCount = 1;

        $hardware = new stdClass();
        $hardware->domain = "test.com";
        $hardware->hostname = "thisIsTest";
        $container->hardware = $hardware;

        $order->orderContainers = array();
        $order->orderContainers[0] = $container;
        print_r($order);
        $result = $client->verifyOrder($order);
        print_r($result);
    }
}


$example = new Example();
// $example->getAllPackages();

// Your package needs to have both activeRamItems and activeServerItems to be orderable.
// $example->getActiveRamItems(273);
// $example->getActiveServerItems(273);

//All price ids are from this function
// $example->getPackageById(273,0,1);

$example->placeOrder();    

```
