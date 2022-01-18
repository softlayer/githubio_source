---
title: "delete_notification_subscriber.go"
description: "delete_notification_subscriber.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```go
/*
Delete a notification subscription

The script deletes a notification for a determinate user in a determinate Virtual Guest for more
reference see these reference pages.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/deleteObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	/*
	Build a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object which contains
	the id we wish to delete. To get the notifications for an determinate Virtual Guest call
	the getObject method using the "mask[monitoringUserNotification]"
	*/
	notifications := []datatypes.User_Customer_Notification_Virtual_Guest{
		{ Id: sl.Int(10056635) },
	}

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer_Notification_Virtual_Guest service
	customerNotificationService := services.GetUserCustomerNotificationVirtualGuestService(sess)

	// Delete selected subscriptions
	result, err := customerNotificationService.DeleteObjects(notifications)
	if err != nil {
		fmt.Printf("\n Unable to delete subscription\n - %s\n", err)
		return
	}

	fmt.Println(result)
}
```
