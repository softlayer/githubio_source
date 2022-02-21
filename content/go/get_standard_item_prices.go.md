---
title: "get_standard_item_prices.go"
description: "get_standard_item_prices.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```go
/*
Retrieve standard item prices from a package.

This script retrieves standard prices from a package. All standard prices don't have an specific
location, taking account this last, we'll retrieve all prices that have 'locationGroupId' IS NULL.
See below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
https://sldn.softlayer.com/article/object-Masks
https://sldn.softlayer.com/article/object-filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
	"github.com/softlayer/softlayer-go/filter"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of package you wish to get information
	packageId := 46             // Virtual Server Instance

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package service
	service := services.GetProductPackageService(sess)

	// Declare object mask in order to get specific data
	mask := "id,hourlyRecurringFee,laborFee,recurringFee,item"

	// Declare filter in order to get all item prices with locationGroupId = NULL
	filter := filter.Path("itemPrices.locationGroupId").IsNull().Build()

	// Call the getItemPrices() method to get item prices according to filter.
	itemPrices, err := service.Id(packageId).Mask(mask).Filter(filter).GetItemPrices()
	if err != nil {
		fmt.Printf("\n Unable to retrieve item prices from package:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,item := range itemPrices {
		jsonFormat, jsonErr := json.Marshal(item)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
