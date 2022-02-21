---
title: "get_server_cost.go"
description: "get_server_cost.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
    - "SoftLayer_Hardware_Server"
tags:
    - "billing"
---


```go
/*
Get the recurring cost of all hardware servers in the account.

Get a list of servers on a SoftLayer account along with their recurring monthly costs. We can
get that by calling to the getHardware() method in the SoftLayer_Account API service, and using
object masks we'll retrieve the ID of all SoftLayer_Hardware objects. Then through a loop we will
call getObject() in SoftLayer_Hardware_Server service with a mask to retrieve the cost.
See below for more information.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
https://sldn.softlayer.com/article/object-Masks

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
	// SoftLayer API username and key.
	username := "set me"
	apikey   := "set me"

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account and service SoftLayer_Hardware_Server services.
	accountService  := services.GetAccountService(sess)
	hardwareService := services.GetHardwareServerService(sess)

	// Object mask to get the id of all SoftLayer_Hardware objects from account.
	mask := "id"

	// Object mask to get hostname, domain, cost, etc., of SoftLayer_Hardware_Server objects.
	serverMask := "id;hostname;domain;fullyQualifiedDomainName;cost"

	// Call SoftLayer_Account::getHardware() method to get all SoftLayer_Hardware objects in the account.
	hardwareList, err := accountService.Mask(mask).GetHardware()
	if err != nil {
		fmt.Printf("\n Unable to retrieve Softlayer_Hardware objects \n -%s", err)
		return
	}

	// For each SoftLayer_Hardware object we'll get data of SoftLayer_Hardware_Server.
	for _, hardware := range hardwareList {
		// Call SoftLayer_Hardware_Server::getObject() in order to get information based on mask.
		server, err := hardwareService.Id(*hardware.Id).Mask(serverMask).GetObject()
		if err != nil {
			fmt.Printf("\n Unable to retrieve Softlayer_Hardware_Server object\n -%s", err)
			return
		}

		// Following helps to print the result in JSON format.
		jsonFormat, jsonErr := json.MarshalIndent(server, "", "     ")
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Printf("\n%s", string(jsonFormat))
	}
}

```
