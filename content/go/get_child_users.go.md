---
title: "get_child_users.go"
description: "get_child_users.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
/*
Get child users.

Retrieve a portal user's child users. Some portal users may not have child users.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getChildUsers
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
  	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of user you want to get his child users
	userId := 167758

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer service
	service := services.GetUserCustomerService(sess)

	// Retrieve all child user from parent user id
	childUsers, err := service.Id(userId).GetChildUsers()
	if err != nil {
		fmt.Printf("\n Unable to retrieve child users - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, user := range childUsers {
		jsonFormat, jsonErr := json.Marshal(user)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
