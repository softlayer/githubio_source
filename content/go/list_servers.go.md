---
title: "list_servers.go"
description: "list_servers.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```
/*
List Bare Metal Servers in the Account

This script gets all hardware servers of Account, on this case we'll use the getHardware()
method of SoftLayer_Account service.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Object-Mask in order to get specific data of server
	mask := "id;hostname;primaryIpAddress;primaryBackendIpAddress;datacenter;" +
		"datacenterName;serviceProvider;hardwareFunctionDescription"

	// Call the getHardware() method.
	hardware, err := service.Mask(mask).GetHardware()
	if err != nil {
		fmt.Printf("\n Unable to get Bare Metal Servers:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,server := range hardware {
		jsonFormat, jsonErr := json.Marshal(server)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
