---
title: "delete_user.go"
description: "delete_user.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
/*
Delete user.

This scripts allows to delete a given user, it retrieves the SoftLayer_User_Customer object
by the SoftLayer_User_Customer::getObject method and changes the status of user to deleted.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
  	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of user you want to delete
	userId := 6660647

	/*
	Build following user structure with the new user status.
	    1001 = Active; 1002 = Disable; 1003 = Inactive; 1021 = Delete ; 1022 = VPN Only
	You can also use call to SoftLayer_User_Customer::getObject and change the status id before
	to pass it to SoftLayer_User_Customer::editObject
	*/
	userTemplate := datatypes.User_Customer {
		UserStatusId: sl.Int(1021),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer service
	service := services.GetUserCustomerService(sess)

	// Call to SoftLayer_User_Customer::editObject in order to delete the user account
	result, err := service.Id(userId).EditObject(&userTemplate)
	if err != nil {
		fmt.Printf("\n Unable to delete selected user - %s\n", err)
		return
	}

  	fmt.Println(result)
}

```
