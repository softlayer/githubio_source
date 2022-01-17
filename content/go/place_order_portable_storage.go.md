---
title: "place_order_portable_storage.go"
description: "place_order_portable_storage.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Disk_Image"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "portablestorage"
---


```go
/*
Order a portable storage

The script orders a portal storage device, it makes a single call to method
SoftLayer_Product_Order::placeOrder.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Disk_Image

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the location, packageId and a description for the portable storage
	// you wish to order
  	location        := "SANJOSE"
  	packageId       := 198    	// Package for order portable storage
  	diskDescription := "SoftLayer Portable Storage"

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(21861) },    // 25 GB (SAN)
	}

	// Build a Container_Product_Order_Virtual_Disk_Image object containing the order
	// you wish to place
	templateObject := datatypes.Container_Product_Order_Virtual_Disk_Image {
		Container_Product_Order : datatypes.Container_Product_Order{
			Location      : sl.String(location),
			PackageId     : sl.Int(packageId),
			Prices        : prices,
		},
		DiskDescription : sl.String(diskDescription),
	}

	// Create a session
  	sess := session.New(username, apikey)

  	// Get SoftLayer_Product_Order service
  	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&templateObject)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
  	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","     ")
  	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
  	}
	fmt.Println(string(jsonFormat))
}

```
