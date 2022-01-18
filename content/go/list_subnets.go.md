---
title: "list_subnets.go"
description: "list_subnets.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet"
tags:
    - "subnets"
---


```go
/*
List subnets. It retrieves all network subnets associated with an account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnets
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"encoding/json"
	"github.com/softlayer/softlayer-go/filter"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	/*
	Filter all subnets by subnetType, following are possible values:
	      PRIMARY_6, GLOBAL_IP, PRIMARY, STATIC_IP_ROUTED,
	      SECONDARY_ON_VLAN, ADDITIONAL_PRIMARY
	On this case we'll filter by 'PRIMARY' type.
	*/
	filter := filter.Path("subnets.subnetType").Eq("PRIMARY").Build()

	// Call method getSubnets() in order to get all subnets in the Account.
	subnets, err := service.Filter(filter).GetSubnets()
	if err != nil {
		fmt.Printf("\n Unable to get subnets:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, subnet := range subnets {
		jsonFormat, jsonErr := json.Marshal(subnet)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```
