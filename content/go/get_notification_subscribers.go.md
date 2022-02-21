---
title: "get_notification_subscribers.go"
description: "get_notification_subscribers.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "users"
---


```go
/*
Get all the notification subscribers for an user.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getSubscribers

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of user you want to get his subscribers
	userId := 437729

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer service
	service := services.GetUserCustomerService(sess)

	// Retrieve the list of subscribers
	subscribers, err := service.Id(userId).GetSubscribers()
	if err != nil {
		fmt.Printf("\n Unable to get subscribers - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, user := range subscribers {
		jsonFormat, jsonErr := json.Marshal(user)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
