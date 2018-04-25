---
title: "reset_portal_user_password.go"
description: "reset_portal_user_password.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
/*
Reset portal user password.

This script resets the password of a portal user by SoftLayer_User_Customer::updatePassword method
need to define the new password and pass it to updatePassword() method.
Take account that users with OpenIdConnect will not be able to update password through this feature.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/updatePassword

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of user you want to add permissions
	userId := 6660647

	// New password you want to set for user.
	// Users with OpenIdConnect (blueId) will not be able to update password through this feature.
	newPassword := "newPassword123!"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer service
	service := services.GetUserCustomerService(sess)

	// Reset the user password by calling to SoftLayer_User_Customer::updatePassword method.
	result, err := service.Id(userId).UpdatePassword(&newPassword)
	if err != nil {
		fmt.Printf("\n Unable to update the user password - %s\n", err)
		return
	} 

  	fmt.Println(result)
}

```
