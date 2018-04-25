---
title: "DeleteNotifications.php"
description: "DeleteNotifications.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```
<?php
/**
 * Example to delete a notification subscription
 * The script deletes an notification for a determinate user in a determinate Virtual Guest
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/deleteObjects
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest
 * 
 * License <http://sldn.softlayer.com/article/License>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * 
 */
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

$userCustomerNotificiation = Softlayer_SoapClient::getClient('SoftLayer_User_Customer_Notification_Virtual_Guest', null, $apiUsername, $apiKey);

/**
 * Build a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object
 * which contains the id we wish to delete
 * To get the notifications for an determinated Virtual Guest
 * call the getObject method + the mask "mask[monitoringUserNotification]"
 * e.g.
 * $guest_id = 7698972;
 * $virtual_guest_service = Softlayer_SoapClient::getClient('SoftLayer_Virtual_Guest', null, $apiUsername, $apiKey);
 * $virtual_guest_service->setObjectMask("mask[monitoringUserNotification]");
 * $virtual_guest_service->setInitParameter($guest_id);
 * $guest = $virtual_guest_service->getObject();
 * print_r($guest);
*/

$notifications = array();
$notification = new stdClass();
$notification->id = 2151450;
$notifications[] = $notification;

try {
    $result = $userCustomerNotificiation->deleteObjects($notifications);
    print_r($result);
} catch (Exception $e) {
    echo 'Unable to delete the notifications: ' . $e->getMessage();
}


?>

```
