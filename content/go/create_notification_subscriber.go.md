---
title: "create_notification_subscriber.go"
description: "create_notification_subscriber.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer_Notification_Virtual_Guests"
    - "SoftLayer_User_Customer_Notification_Virtual_Guest"
tags:
    - "monitoring"
---


```
/*
Create a notification subscription

The script creates a notification for a determinate user in a determinate Virtual Guest
for more reference see these reference pages

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_Notification_Virtual_Guest/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_Notification_Virtual_Guests

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
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	/*
	Build a SoftLayer_User_Customer_Notification_Virtual_Guest skeleton object which contains
	the virtual guest id and user id of the notification.
	*/
	notification := datatypes.User_Customer_Notification_Virtual_Guest{
		GuestId: sl.Int(33051333),
		UserId:  sl.Int(6625205),
	}

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer_Notification_Virtual_Guests service
	customerNotificationService := services.GetUserCustomerNotificationVirtualGuestService(sess)

	// Create a new subscription
	subscription, err := customerNotificationService.CreateObject(&notification)
	if err != nil {
		fmt.Printf("\n Unable to create subscription\n - %s\n", err)
		return
	}

	// Following helps to print results in JSON format
	jsonFormat, jsonErr := json.MarshalIndent(subscription, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}
```
