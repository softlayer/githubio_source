---
title: "disableServersAndUser.php"
description: "disableServersAndUser.php"
date: "2018-04-25"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_SoapClient"
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Guest"
tags:
    - "users"
---


```php
<?php
require_once ('Softlayer/SoapClient.class.php');
 
$apiUsername = '';
$apiKey = 'apikey_goes_here';
 
$accountClient = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);
$userClient = SoftLayer_SoapClient::getClient('SoftLayer_User_Customer', null, $apiUsername, $apiKey);
$virtualGuestClient = SoftLayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $apiUsername, $apiKey);
 
$accountClient->setObjectMask("mask[id, userStatus, username]");
$users = $accountClient->getUsers();
var_dump($users);
 
$userToDisable = 'username';

#$ccis = $userClient->getVirtualGuests();
#print ($ccis);
 
// Loop through each user on the account and identify by username
foreach ($users as $user) {
    if ($user->username == $userToDisable) {
        // set the userId for the userClient
        $userClient->setInitParameter($user->id);
 
        // Shutdown a users CCIs
        $ccis = $userClient->getVirtualGuests();
        foreach ($ccis as $cci) {
            $virtualGuestClient->setInitParameter($cci->id);
        #    $virtualGuestClient->powerOffSoft();
            print ($virtualGuestClient);
        }
 
        // Disable the user
        $templateObject = new stdClass();
        $templateObject->id = $user->id;
        $templateObject->userStatusId = 1002; // 1001 for enabled   
        #$result = $userClient->editObject($templateObject);
    }
}
?>
```
