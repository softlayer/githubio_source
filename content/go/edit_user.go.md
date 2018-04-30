---
title: "edit_user.go"
description: "edit_user.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```
/*
Edit User.

Account master users and sub-users who have the User Manage permission in the SoftLayer customer portal
can update other user's information. Use editObject() if you wish to edit a single user account.
Users who do not have the User Manage permission can only update their own information.

Important manual Pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer

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
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of user you want to delete
	userId := 6660647

	// Build the user structure with the new information about the user.
	userTemplate := datatypes.User_Customer {
		FirstName    : sl.String("firstname0A"),
		LastName     : sl.String("lastname0A"),
		Email        : sl.String("user0A_mail@softlayer.local"),
		Address1     : sl.String("Address 0A"),
		CompanyName  : sl.String("Some Company 0A"),
		City         : sl.String("Houston"),
		OfficePhone  : sl.String("4422335"),
		PostalCode   : sl.String("5500"),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer service
	service := services.GetUserCustomerService(sess)

	// Update user account with the new information
  	result, err := service.Id(userId).EditObject(&userTemplate)
	if err != nil {
		fmt.Printf("\n Unable to edit selected user:\n - %s\n", err)
		return
	}

	// Print result
	fmt.Printf("\nUser edit: %t", result)
	fmt.Println("\nFollowing is the new user information")

	// Define object-mask used to retrieve specific data information about user
	mask := "id;username;firstName;lastName;email;address1;companyName;country;city;" +
		"state;officePhone;postalCode;timezone;userStatus"

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
