---
title: "get_item_prices.go"
description: "get_item_prices.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
tags:
    - "package"
---


```
/*
Retrieve item prices from a package.

This example retrieves the general information about product item prices from an specific package.
See below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
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

	// The id of package you wish to get its item prices
	packageId := 46             // Virtual Server Instance

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package service
	service := services.GetProductPackageService(sess)

	// Declare object mask in order to get specific data
	mask := "id,hourlyRecurringFee,laborFee,recurringFee,item"

	// Call the getItemPrices() method.
	itemPrices, err := service.Id(packageId).Mask(mask).GetItemPrices()
	if err != nil {
		fmt.Printf("\n Unable to retrieve Item Prices from Package:\n - %s\n", err)
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
