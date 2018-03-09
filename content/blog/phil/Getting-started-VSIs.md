---
title: "Getting started with VSI's"
description: "In the context of the SoftLayer API, SoftLayer Virtual Server Instances(VSIs) are represented by [[SoftLayer_Virtual_Gue"
date: "2013-04-18"
author: "phil"
tags:
    - "blog"
---

In the context of the SoftLayer API, SoftLayer Virtual Server Instances(VSIs) are represented by [[SoftLayer_Virtual_Guest (type)]] objects. The [[SoftLayer_Virtual_Guest]] service allows for interaction with a specific VSI and you are able to interact with all VSIs on your account through the [[SoftLayer_Account]] service. You will want to make sure you are on the latest version of the [Softlayer PHP API SoapClient](https://github.com/softlayer/softlayer-api-php-client).

## Creating
Ordering new VSIs is accomplished through [[SoftLayer_Virtual_Guest::createObject]].
First, a SoftLayer_Virtual_Guest template object is created that contains the details of the VSI. Every VSI template object will need, at minimum, the following properties defined:

* hostname - Hostname of the new VSI
* domain - Domain name of the new VSI
* startCpus - Number of processing cores
* maxMemory - Memory allocation in MB
* datacenter - A datacenter class and the datacenter name
* hourlyBillingFlag - Set true for hourly billing, false for monthly
* operatingSystemReferenceCode - Code to specify which OS to install
* localDiskFlag - Setting to true will configure a VSI with local disks, false for SAN disks

<php>
require_once __DIR__.'/vendor/autoload.php';

$user = 'set me';
$key = 'set me';

$virtualGuestClient = \\SoftLayer\\SoapClient::getClient('SoftLayer_Virtual_Guest', null, $user, $key);
$virtualGuestTemplate = new stdClass();
$virtualGuestTemplate->hostname = 'test1';
$virtualGuestTemplate->domain = 'example.com';
$virtualGuestTemplate->startCpus = 1;
$virtualGuestTemplate->maxMemory = 1024;
$virtualGuestTemplate->datacenter = new stdClass();
$virtualGuestTemplate->datacenter->name = 'dal05';
$virtualGuestTemplate->hourlyBillingFlag = true;
$virtualGuestTemplate->operatingSystemReferenceCode = 'UBUNTU_LATEST';
$virtualGuestTemplate->localDiskFlag = false;

$result = $virtualGuestClient->createObject($virtualGuestTemplate);
print_r($result);
</php>
All options for VSI ordering can be retrieved with [[SoftLayer_Virtual_Guest::getCreateObjectOptions]].
The [[SoftLayer_Virtual_Guest::createObject|createObject()]] method incurs charges on the account so it is best to test VSI creation without causing an order to be placed with [[SoftLayer_Virtual_Guest::generateOrderTemplate]] to generate an order object. The [[SoftLayer_Container_Product_Order (type)]] returned by this method can be passed into [[SoftLayer_Product_Order::verifyOrder]] which informs of any issues that would prevent the order from processing.
<php>
$orderClient = \\SoftLayer\\SoapClient::getClient('SoftLayer_Product_Order', Null, $user, $key);
$orderContainer = $virtualGuestClient->generateOrderTemplate($virtualGuestTemplate);
print_r($orderClient->verifyOrder($orderContainer);
</php>
## Listing
A list of all Virtual Server Instances can be gathered from the [[SoftLayer_Account]] service with the [[SoftLayer_Account::getVirtualGuests]] method. This method returns an array of [[SoftLayer_Virtual_Guest (type)]] data type objects.
<php>
$accountClient = \\SoftLayer\\SoapClient::getClient('SoftLayer_Account', Null, $user, $key);
$virtualGuests = $accountClient->getVirtualGuests();
print_r($virtualGuests);
</php>
This full listing is often used for retrieving information about all VSIs on an account and is also useful when searching for a specific VSI whos ID is unknown.
<php>
$accountClient = \\SoftLayer\\SoapClient::getClient('SoftLayer_Account', Null, $user, $key);
$virtualGuests = $accountClient->getVirtualGuests();
foreach ($virtualGuests as $virtualGuest) {
    if ($virtualGuest->hostname == "server1") {
        $serverId = $virtualGuest->id;
    }
}
</php>
## Details
To get information about a specific VSI we can use [[SoftLayer_Virtual_Guest::getObject]] which returns a [[SoftLayer_Virtual_Guest (type)]] object. [[Object masks]] can be used to include data outside of [[SoftLayer_Virtual_Guest (type)|SoftLayer_Virtual_Guest's]] local properties. Below is an example of using getObject on the SoftLayer_Virtual_Guest service with an object mask which  provides the passwords for the operating system installed on the server.
<php>
$guestClient = \\SoftLayer\\SoapClient::getClient('SoftLayer_Virtual_Guest', $id, $user, $key);
$objectMask = "mask[id, hostname, domain, operatingSystem[passwords]]";
$guestClient->setObjectMask($objectMask);
$virtualGuest = $guestClient->getObject();
print_r($virtualGuest);
</php>
Since we have also defined a number of local properties, notice the output only includes the limited set of local properties defined in the mask in addition to the relational properties brought in by the object mask.
## Canceling
Canceling VSIs can be done by pulling the ID from the SoftLayer_Account service. In this example we pull all virtual guests from the account and use the hostname to parse the specific guest we want to cancel. This should be used with caution as the hostname of a virtual guest is not unique.
SoftLayer_Virtual_Guest::deleteObject
<php>
$guestClient = \\SoftLayer\\SoapClient::getClient('SoftLayer_Virtual_Guest', $id, $user, $key);
$result = $guestClient->deleteObject();
print_r($result);
</php>
This method immediately cancels the computing instance with the specified ID.
Note: Pausing an instance with [[SoftLayer_Virtual_Guest::pause]] will not stop billing. An instance must be cancelled/destroyed for billing to cease.
## Rebooting
Power cycling a VSI can be done two ways:

* [[SoftLayer_Virtual_Guest::rebootHard]] - Removing and reapplying the power source
* [[SoftLayer_Virtual_Guest::rebootSoft]] - Attempt to reboot the device with an OS level command


