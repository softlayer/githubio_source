---
title: "create_customer.go"
description: "create_customer.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```
/*
Create a customer.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Brand/createCustomerAccount
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	//Bypass validation for duplicate account
	byPassDuplicateAccountCheck := sl.Bool(false)

	// Build the skeleton of SoftLayer_Account object with the account's information
	templateObject := datatypes.Account{
		CompanyName : sl.String("My company"),
		Email       : sl.String("email@example.com"),
		Address1    : sl.String("Address 1"),
		Country     : sl.String("US"),
		State       : sl.String("TX"),
		City        : sl.String("Ohio"),
		FirstName   : sl.String("First Name"),
		LastName    : sl.String("Last Name"),
		OfficePhone : sl.String("A Number"),
		PostalCode  : sl.String("A Postal Number"),
		BrandId     : sl.Int(4),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Brand service
	service := services.GetBrandService(sess)

	// Create new customer
	customer, err := service.CreateCustomerAccount(&templateObject, byPassDuplicateAccountCheck)
	if err != nil {
		fmt.Printf("\n Unable to get subscribers - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(customer, "","    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
