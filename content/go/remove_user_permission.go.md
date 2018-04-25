---
title: "remove_user_permission.go"
description: "remove_user_permission.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "users"
---


```
/*
Remove user permission.

This script shows how to remove permissions to an user.

Important manual Pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/removePortalPermission
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of user you want to remove permissions
	userId := 6660647

	/*
	Declare the permission you want to remove.
	Use SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects method to retrieve
	a list of all available permissions.
	*/
	permission := datatypes.User_Customer_CustomerPermission_Permission {
		KeyName : sl.String("TICKET_ADD"),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer service
	service := services.GetUserCustomerService(sess)

	// Add single permission to user
	result, err := service.Id(userId).RemovePortalPermission(&permission)
	if err != nil {
		fmt.Printf("\n Unable to add permissions to user - %s\n", err)
		return
	}

	// Print result
	fmt.Printf("\nUser edit: %t", result)
	fmt.Println("\nFollowing is the new user information:")

	// Define object-mask used to retrieve specific data information about user
	mask := "id;username;firstName;lastName;permissions"

	// Retrieve and check if new information was successfully changed
	user, err := service.Id(userId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to retrieve selected user:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(user,"","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
