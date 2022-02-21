---
title: "create_standard_firewall.go"
description: "create_standard_firewall.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
tags:
    - "firewalls"
---


```go
/*
Create a standard firewall

This script order a firewall service on a virtual instance using the SoftLayer_Product_Order::placeOrder
method. First we'll build a skeleton of a SoftLayer_Container_Product_Order_Network_Protection_Firewall
object, providing the ID of virtual instance in which the firewall service will be configured.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the package id, quantity, and guest id for the Firewall you wish to order
	complexType := "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
	quantity    := 1
	packageId   := 0
	guestId     := 27395815

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItemPrices method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(408) },          // 1000Mbps Hardware Firewall
	}

	// Build a skeleton Container_Product_Order object containing the order you wish to place.
	templateObject := datatypes.Container_Product_Order {
		ComplexType   : sl.String(complexType),
		Prices        : prices,
		PackageId     : sl.Int(packageId),
		Quantity      : sl.Int(quantity),
		VirtualGuests : []datatypes.Virtual_Guest{
			{Id: sl.Int(guestId)},
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
