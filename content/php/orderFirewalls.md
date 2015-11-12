---
title: "Order Firewall and Security Appliances"
description: "An example of how to order a hardware firewall and a FortiGate security appliance"
date: "2015-11-11"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated"
tags:
    - "ordering"
    - "firewall"
    - "placeOrder"
    - "FortiGate"
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


    function getPackageById($id=0, $onlyShow=0, $showPrices=1) {
        $packageClient = \SoftLayer\SoapClient::getClient('SoftLayer_Product_Package', $id, $this->apiUsername, $this->apiKey );
        $package = $packageClient->getItems();
        print "ID, KeyName, Description \n";
        foreach ($package as $item) {
            if ($onlyShow == 0 || $onlyShow == $item->id) {
                print $item->id . " , " . $item->keyName . " , " . $item->description . "\n" ;
                if($showPrices) {
                    print_r($item->prices); 
                }
            }
        }
    }

    function placeOrderHardwareFirewall() {
        // http://sldn.softlayer.com/blog/phil/Getting-Started-Firewalls
        // The speed of the firewall needs to match speed of the server
       
        // 3896 , HARDWARE_FIREWALL_HIGH_AVAILABILITY , Hardware Firewall (High Availability)
        // 297 , 1000MBPS_HARDWARE_FIREWALL , 1000Mbps Hardware Firewall
        // 298 , 100MBPS_HARDWARE_FIREWALL , 100Mbps Hardware Firewall
        // 1296 , 2000MBPS_HARDWARE_FIREWALL , 2000Mbps Hardware Firewall
        // 4550 , 20MBPS_HARDWARE_FIREWALL , 20Mbps Hardware Firewall
        // 299 , 10MBPS_HARDWARE_FIREWALL , 10Mbps Hardware Firewall
        // 1329 , HARDWARE_FIREWALL_DEDICATED , Hardware Firewall (Dedicated)
        // 4551 , 200MBPS_HARDWARE_FIREWALL , 200Mbps Hardware Firewall
        // $example->getPackageById(0, 297 );
        // Generic Location Price
        // (
        //  [id] => 408
        //  [itemId] => 297
        //  [locationGroupId] =>
        //  [oneTimeFee] => 0
        //  [recurringFee] => 199
        //  [setupFee] => 0
        // )
        $client = \SoftLayer\XmlRpcClient::getClient('SoftLayer_Product_Order', null, $this->apiUsername, $this->apiKey );
        $order = new stdClass();

        $price = new stdClass();
        $price->id = 408;

        // http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall/
        $container = new stdClass();
        $container->complexType = "SoftLayer_Container_Product_Order_Network_Protection_Firewall";
        $container->packageId = 0;
        $container->quantity = 1;
        $container->prices = array($price);
        $container->hardware = array();

        // Put your serverId here
        $serverToFirewall = new stdClass();
        $serverToFirewall->id = 12345;
        $container->hardware[0] = $serverToFirewall;

        $order->orderContainers = array();
        $order->orderContainers[0] = $container;
        $result = $client->verifyOrder($order);
        print_r($result);
    }


    function placeOrderFortigateAppliance() {
        // The speed of the firewall needs to match speed of the server
        // $example->getPackageById(0, 4337 );
        // 4337 , FORTIGATE_SECURITY_APPLIANCE , FortiGate Security Appliance
        // 4338 , FORTIGATE_SECURITY_APPLIANCE_HIGH_AVAILABILITY , FortiGate Security Appliance (High Availability)
        // Generic Location Price
        // [id] => 21514
        // [itemId] => 4337
        // [locationGroupId] =>
        // [recurringFee] => 999
        $client = \SoftLayer\XmlRpcClient::getClient('SoftLayer_Product_Order', null, $this->apiUsername, $this->apiKey );
        $order = new stdClass();

        $price = new stdClass();
        $price->id = 21514;

        // http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated/
        $container = new stdClass();
        $container->complexType = "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated";
        $container->packageId = 0;
        $container->quantity = 1;
        $container->prices = array($price);
        $container->hardware = array();
        // Put the vlan id that you want to protect here
        $container->vlanId = 12345;

        $order->orderContainers = array();
        $order->orderContainers[0] = $container;
        $result = $client->verifyOrder($order);
        print_r($result);
    }

}


$example = new Example();
// $example->getAllPackages();
// $example->getPackageById(0, 297 );
// $example->placeOrderHardwareFirewall();
// $example->getPackageById(0, 4337 );
// $example->placeOrderFortigateAppliance();    

```
