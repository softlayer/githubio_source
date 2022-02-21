---
title: "get_item_prices_by_location.go"
description: "get_item_prices_by_location.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```go
/*
Get item prices by location

This script retrieves item prices of a package for a datacenter location.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
https://sldn.softlayer.com/article/sbject-Filters

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
	packageId := 200

	/*
	The location name you want to get item prices. Following are some locations you can use:
	   Amsterdam 1, Amsterdam 3, Chennai 1, Frankfurt 2, Hong Kong 2, London 1, London 2,
	   Melbourne 1, Mexico 1, Milan 1, Montreal 1, Oslo 1, Paris 1, Sao Paulo 1, Seoul 1,
	   Singapore 1, Sydney 1, Sydney 4, Toronto 1, Tokyo 2
	 */
	location := "Oslo 1"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package service
	service := services.GetProductPackageService(sess)

	// Declare object mask in order to get specific data
	mask := "id,hourlyRecurringFee,laborFee,recurringFee,item,pricingLocationGroup[id,locations[longName]]"

	// Declare filter to get item prices for an specific location
	filter := filter.Path("itemPrices.pricingLocationGroup.locations.longName").Eq(location).Build()

	// Call to getItemPrices() method in order to get prices according to filter.
	itemPrices, err := service.Id(packageId).Mask(mask).Filter(filter).GetItemPrices()
	if err != nil {
		fmt.Printf("\n Unable to get item prices :\n - %s\n", err)
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
