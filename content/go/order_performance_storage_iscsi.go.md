---
title: "order_performance_storage_iscsi.go"
description: "order_performance_storage_iscsi.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi"
    - "SoftLayer_Product_Order"
tags:
    - "blockstorage"
---


```go
/*
Order Performance Storage iSCSI.

This script creates an order for Performance Storage iSCSI, for that we'll build a
SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi object and pass it to
SoftLayer_Product_Order::placeOrder method.
See below references for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_PerformanceStorage_Iscsi

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
	username    := "set me"
  	apikey      := "set me"

	// Declare the complexType, location, packageId and quantity for the storage
	// you wish to order
  	quantity    := 1
  	location    := "DALLAS09"
  	packageId   := 222
  	osKeyName   := "LINUX"

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
  	prices := []datatypes.Product_Item_Price {
		{ Id: sl.Int(40672) },  // Block Storage Performance (ISCSI)
		{ Id: sl.Int(40682) },  // 20 GB Storage Space
		{ Id: sl.Int(40792) },  // 100 IOPS
  	}

	// This should match the OS type of the host(s) that will connect to the volume.
	// The only required property is the keyName.
	osFormatType := &datatypes.Network_Storage_Iscsi_OS_Type {
		KeyName: sl.String(osKeyName),
	}

	// Build a Container_Product_Order_Network_PerformanceStorage object
	storageOrder := datatypes.Container_Product_Order_Network_PerformanceStorage {
		Container_Product_Order : datatypes.Container_Product_Order {
			Quantity      : sl.Int(quantity),
			Location      : sl.String(location),
			PackageId     : sl.Int(packageId),
			Prices        : prices,
		},
	}

	// Build a Container_Product_Order_Network_PerformanceStorage_Iscsi object containing
	// the order you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_PerformanceStorage_Iscsi {
		Container_Product_Order_Network_PerformanceStorage : storageOrder,
		OsFormatType                                       : osFormatType,
	}

	// Create a session.
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service.
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
