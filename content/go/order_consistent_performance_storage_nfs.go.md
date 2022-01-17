---
title: "order_consistent_performance_storage_nfs.go"
description: "order_consistent_performance_storage_nfs.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs"
tags:
    - "blockstorage"
---


```go
/*
Order Consistent Performance Storage Nfs.

This script creates an order for Consistent Performance Storage Nfs (Monthly)
See below references for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_PerformanceStorage_Nfs

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
	username := "set-me"
  	apikey   := "set-me"

	// Declare the complexType,location, packageId and quantity for the storage
	// you wish to order
	quantity    := 1
  	location    := "DALLAS09"
  	packageId   := 222          // Performance Storage

  	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
  	prices := []datatypes.Product_Item_Price {
    		{ Id: sl.Int(40662) },  // File Storage Performance (Nfs)
    		{ Id: sl.Int(40682) },  // 20 GB Storage Space
    		{ Id: sl.Int(40792) },  // 100 IOPS
  	}

	// Build the Container_Product_Order_Network_PerformanceStorage object
	storageOrder := datatypes.Container_Product_Order_Network_PerformanceStorage {
		Container_Product_Order : datatypes.Container_Product_Order {
			Quantity      : sl.Int(quantity),
			Location      : sl.String(location),
			PackageId     : sl.Int(packageId),
			Prices        : prices,
		},
	}

	// Build a Container_Product_Order_Network_PerformanceStorage_Nfs object containing
	// the order you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_PerformanceStorage_Nfs {
    		Container_Product_Order_Network_PerformanceStorage : storageOrder,
	}

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("%s\n", err)
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
