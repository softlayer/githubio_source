---
title: "list_agents.go"
description: "list_agents.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
tags:
    - "brands"
---


```go
/*
List agents.

The script retrieves all the agents in a brand account.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer

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

	// The id of Brand you wish to retrieve his agents
	brandId := 2

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Brand service
	service := services.GetBrandService(sess)

	mask := "id,firstName,lastName,username,email,userStatus[name]"

	// Retrieve agents
	accounts, err := service.Id(brandId).Mask(mask).Limit(100).GetUsers()
	if err != nil {
		fmt.Printf("\n Unable to retrieve agents - %s\n", err)
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
