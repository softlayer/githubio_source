---
title: "order_endurance_storage.go"
description: "order_endurance_storage.go"
date: "2018-04-25"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Enterprise"
tags:
    - "blockstorage"
---


```go
/*
Order a block storage (endurance)

The script orders a block storage (endurance) device, with 40GB storage and 0.25 IOPS, it makes a
single call to SoftLayer_Product_Order::verifyOrder method which can be replaced by placeOrder().

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Enterprise
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := ""
	apikey   := "apikey_goes_here"

	// Declare the location, packageId and quantity for the storage you wish to order
	quantity := 1
	location := "MEXICO"
	packageId := 240
	osKeyName := "LINUX"

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItemPrices method
	prices := []datatypes.Product_Item_Price {
		{ Id: sl.Int(45098) },  // Block Storage
		{ Id: sl.Int(45058) },  // Endurance Storage
		{ Id: sl.Int(45148) },  // 40 GB Storage Space
		{ Id: sl.Int(45068) },  // 0.25 IOPS per GB
	}

	// This should match the OS type of the host(s) that will connect to the volume.
	// The only required property is the keyName.
	osFormatType := &datatypes.Network_Storage_Iscsi_OS_Type {
		KeyName: sl.String(osKeyName),

	}

	// Build a Container_Product_Order_Network_PerformanceStorage object
	templateOrder := datatypes.Container_Product_Order_Network_Storage_Enterprise {
		Container_Product_Order : datatypes.Container_Product_Order {
			Quantity      : sl.Int(quantity),
			Location      : sl.String(location),
			PackageId     : sl.Int(packageId),
			Prices        : prices,
		},
		OsFormatType: osFormatType,
	}

	// Create a session.
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service.
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&templateOrder)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt,"","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
