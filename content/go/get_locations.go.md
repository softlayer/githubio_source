---
title: "get_locations.go"
description: "get_locations.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```go
/*
Get package location.

This script will retrieve a collection of valid locations for a given package
by calling to SoftLayer_Product_Package::getLocations method.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getLocations

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

	// The id of package you wish to get its item prices
	packageId := 46             // Virtual Server Instance

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package service
	service := services.GetProductPackageService(sess)

	// Call the getItemPrices() method.
	locations, err := service.Id(packageId).GetLocations()
	if err != nil {
		fmt.Printf("\n Unable to retrieve Item Prices from Package:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,location := range locations {
		jsonFormat, jsonErr := json.Marshal(location)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
