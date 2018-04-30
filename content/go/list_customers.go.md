---
title: "list_customers.go"
description: "list_customers.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```
/*
List customers.

The script retrieves all the customers in a brand account.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Brand/getOwnedAccounts
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
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

	// The id of Brand you wish to retrieve his accounts
	brandId := 2

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Brand service
	service := services.GetBrandService(sess)

	// Declare mask in order to get specific data of accounts
	mask := "accountStatus[name],masterUser[username],hardwareCount,virtualGuestCount," +
		"userCount,openTicketCount"

	// Get accounts in the brand
	accounts, err := service.Id(brandId).Mask(mask).GetOwnedAccounts()
	if err != nil {
		fmt.Printf("\n Unable to get accounts - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, account := range accounts {
		jsonFormat, jsonErr := json.Marshal(account)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
