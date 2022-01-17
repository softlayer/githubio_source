---
title: "create_user.go"
description: "create_user.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
tags:
    - "users"
---


```go
/*
Create user

The script creates an user, it makes a single call to the SoftLayer_User_Customer::createObject
method. For more information see below.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Build the skeleton of new user like below
	userTemplate := datatypes.User_Customer {
		ParentId     : sl.Int(6625205),
		Username     : sl.String("user01"),
		FirstName    : sl.String("firstname"),
		LastName     : sl.String("lastname"),
		Email        : sl.String("user01_mail@softlayer.local"),
		Address1     : sl.String("Address 01"),
		CompanyName  : sl.String("Some Company"),
		Country      : sl.String("US"),
		City         : sl.String("Dallas"),
		State        : sl.String("TX"),
		OfficePhone  : sl.String("4422335"),
		PostalCode   : sl.String("2500"),
		TimezoneId   : sl.Int(114),
		UserStatusId : sl.Int(1001),
	}

	// Set the password of user
	password := "Password!123"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_User_Customer service
	service := services.GetUserCustomerService(sess)

	// Call to createObject() method in order to create the new user account
	user, err := service.CreateObject(&userTemplate, &password, &password)
	if err != nil {
		fmt.Printf("\n Unable to create new user:\n - %s\n", err)
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
