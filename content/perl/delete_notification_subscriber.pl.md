---
title: "delete_notification_subscriber.pl"
description: "delete_notification_subscriber.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```
# Delete a notification subscription
# 
# The script deletes a notification for a determinate user in a determinate Virtual Guest
# for more reference see these reference pages
# 
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/deleteObjects
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Building a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object
# wich contains the id we wish to delete
# To get the notifications for an determinated Virtual Guest
# call the getObject method + the mask "mask[monitoringUserNotification]"
# e.g.
# my $guest_id = 7698972;
# my $virtual_guest_service = SoftLayer::API::SOAP->new('SoftLayer_Virtual_Guest', undef, $username, $key);
# $virtual_guest_service->setObjectMask("mask[monitoringUserNotification]");
# $virtual_guest_service->setInitParameter($guest_id);
# my $guest = $virtual_guest_service->getObject();
# print Dumper($guest->result);
my $notification = [
    bless({
        'id' => 2147546,
    },'slapi:SoftLayer_User_Customer_Notification_Virtual_Guest')
];

# Creating a SoftLayer API client object
my $user_customer_notificiation = SoftLayer::API::SOAP->new('SoftLayer_User_Customer_Notification_Virtual_Guest', undef, $username, $key);

my $result = $user_customer_notificiation->deleteObjects($notification);
if ($result->fault) {
    die 'Unable to delete the notification subscribers. ' . $result->faultstring;
}
print Dumper($result->result);

```
