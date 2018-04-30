---
title: "place_order_cdn.go"
description: "place_order_cdn.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
/*
Order a new CDN account

Build a SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object for a new CDN
account order and pass it to the SoftLayer_Product_Order service to order it. In this case we'll
order a pay as you go bandwidth and storage CDN account. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the package id and quantity for the cdn you wish to order
	packageId := 208
	quantity  := 1

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItemPrices method
	prices := []datatypes.Product_Item_Price{
		{Id: sl.Int(1661)},		// CDN Pay as You Go Bandwidth
		{Id: sl.Int(1670)},		// CDN No storage (origin pull)
	}
	// Build a skeleton SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object
	// containing the order you wish to place.
	templateObject := datatypes.Container_Product_Order_Network_ContentDelivery_Account{
		Container_Product_Order: datatypes.Container_Product_Order{
			PackageId : sl.Int(packageId),
			Quantity  : sl.Int(quantity),
			Prices    : prices,
		},
	}

	// Create SoftLayer API session
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
	jsonFormat, jsonErr := json.MarshalIndent(receipt,"","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
