---
title: "order_endurance_storage.go"
description: "order_endurance_storage.go"
date: "2023-03-10"
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

	// Create a session.
	sess := session.New(username, apikey)

	// To get item prices and regions and order an endurance storage package ID is required
	enduranceStoragePackageID := 240

	// This method will return all regions where the package is available
	getRegions(sess, enduranceStoragePackageID)
	// This method will return all item prices that endurance storage package has available
	getItemPrices(sess, enduranceStoragePackageID)
	// This method will build a template to order an endurance storage and verify it
	VerifyOrder(sess, enduranceStoragePackageID)

}

func getRegions(sess *session.Session, enduranceStoragePackageID int) {
	// Get SoftLayer_Product_Package service.
	service := services.GetProductPackageService(sess)

	// Use GetRegions() method to return all regions where the package is available
	regions, err := service.Id(enduranceStoragePackageID).GetRegions()
	if err != nil {
		fmt.Printf("\n Unable to get regions:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(regions, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

func getItemPrices(sess *session.Session, enduranceStoragePackageID int) {
	// Get SoftLayer_Product_Package service.
	service := services.GetProductPackageService(sess)

	// Use GetItemPrices() method to return all item prices that endurance storage package has available
	itemPrices, err := service.Id(enduranceStoragePackageID).GetItemPrices()
	if err != nil {
		fmt.Printf("\n Unable to get item prices:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(itemPrices, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

func VerifyOrder(sess *session.Session, enduranceStoragePackageID int) {
	// Get SoftLayer_Product_Order service.
	service := services.GetProductOrderService(sess)

	// Declare the location, packageId and quantity for the storage you wish to order
	// Use getRegions method to see other locations
	quantity := 1
	location := "TORONTO"
	packageId := 240
	osKeyName := "LINUX"

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItemPrices method
	prices := []datatypes.Product_Item_Price{
		{Id: sl.Int(45098)}, // Block Storage
		{Id: sl.Int(45058)}, // Endurance Storage
		{Id: sl.Int(45148)}, // 40 GB Storage Space
		{Id: sl.Int(45068)}, // 0.25 IOPS per GB
	}

	// This should match the OS type of the host(s) that will connect to the volume.
	// The only required property is the keyName.
	osFormatType := &datatypes.Network_Storage_Iscsi_OS_Type{
		KeyName: sl.String(osKeyName),
	}

	// Build a Container_Product_Order_Network_PerformanceStorage object
	templateOrder := datatypes.Container_Product_Order_Network_Storage_Enterprise{
		Container_Product_Order: datatypes.Container_Product_Order{
			Quantity:  sl.Int(quantity),
			Location:  sl.String(location),
			PackageId: sl.Int(packageId),
			Prices:    prices,
		},
		OsFormatType: osFormatType,
	}

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&templateOrder)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
