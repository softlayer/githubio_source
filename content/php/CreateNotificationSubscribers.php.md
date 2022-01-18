---
title: "CreateNotificationSubscribers.php"
description: "CreateNotificationSubscribers.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer_Notification_Virtual_Guestqs"
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```php
<?php
/**
 * Example to create a notification subscription
 * The script creates an notification for a determinate user in a determinate Virtual Guest
 * for more reference see these reference pages
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/createObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guestqs
 * 
 * License <http://sldn.softlayer.com/article/License>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * 
 */
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

# Building a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object
# which contains the virtual guest id and user id of the notification
$newNotifications = array();
$newNotification = new stdClass();
$newNotification->guestId = 7698972;
$newNotification->userId = 205832;
$newNotifications[] = $newNotification;

$userCustomerNotificiation = Softlayer_SoapClient::getClient('SoftLayer_User_Customer_Notification_Virtual_Guest', null, $apiUsername, $apiKey);

try {
    $result = $userCustomerNotificiation->createObjects($newNotifications);
    print_r($result);
} catch (Exception $e) {
    echo 'Unable to create the notification subscribers: ' . $e->getMessage();
}

?>

```
