---
title: "get_bare_metal_billing_items.go"
description: "get_bare_metal_billing_items.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
    - "SoftLayer_Billing_Item"
tags:
    - "billing"
---


```
/*
Retrieve billing items for Bare Metal servers in the account.

This script makes a single call to the getHardware() method in the SoftLayer_Account API service
and uses a object mask to get the billing items and items for each Bare Metal server in the account.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"strings"
	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Declare object mask used to get information about items
	mask := "id;hostname;domain;datacenter[longName];billingItem[item]"

	// Call method getHardware() in order to retrieve billing items of each bare metal server.
	servers, err := service.Mask(mask).GetHardware()
	if err != nil {
		fmt.Printf("\n Unable to retrieve hardware servers:\n - %s\n", err)
		return
	}

	// Following helps to print the result en JSON format.
	for _, hardware := range servers {
		jsonFormat, jsonErr := json.MarshalIndent(hardware, "", "     ")
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Printf("\n%s", string(jsonFormat))
		// Print single separator
		fmt.Printf("\n%s", strings.Repeat("-", 120))
	}
}

```
