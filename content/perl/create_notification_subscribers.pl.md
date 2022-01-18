---
title: "create_notification_subscribers.pl"
description: "create_notification_subscribers.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer_Notification_Virtual_Guests"
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```perl
# 
# Create a notification subscription
# 
# The script creates a notification for a determinate user in a determinate Virtual Guest
# for more reference see these reference pages
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/createObject
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guests
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username.
my $username = 'set me';
my $key = 'set me';

# Building a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object
# which contains the virtual guest id and user id of the notification
my $new_notification = [
    bless({
        'guestId' => 7698972,
        'userId' => 205832
    },'slapi:SoftLayer_User_Customer_Notification_Virtual_Guest')
];

# Creating a SoftLayer API client object
my $user_customer_notificiation = SoftLayer::API::SOAP->new('SoftLayer_User_Customer_Notification_Virtual_Guest', undef, $username, $key);

my $result = $user_customer_notificiation->createObjects($new_notification);
if ($result->fault) {
    die 'Unable to create notification subscribers. ' . $result->faultstring;
}
print Dumper($result->result);

```
