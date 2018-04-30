---
title: "list_servers_to_order_hourly.go"
description: "list_servers_to_order_hourly.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package_Server"
tags:
    - "baremetalservers"
---


```
/*
List all the servers to order (hourly).

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package_Server/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Server/
http://sldn.softlayer.com/article/object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/filter"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package_Server service
	service := services.GetProductPackageServerService(sess)

	// In order to get all 'hourly' servers to order we will use the following filter
	filter := filter.Build(
		filter.Path("packageType").Eq("BARE_METAL_CPU_FAST_PROVISION"),
	)

	// Call the method SoftLayer_Product_Package_Server::getAllObjects
	servers, err := service.Filter(filter).GetAllObjects()
	if err != nil {
		fmt.Printf("\n Unable to list of servers to order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,server := range servers {
		jsonFormat, jsonErr := json.Marshal(server)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```
