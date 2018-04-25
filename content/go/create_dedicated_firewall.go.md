---
title: "create_dedicated_firewall.go"
description: "create_dedicated_firewall.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "firewalls"
---


```
/*
Create a dedicated firewall

This script order a dedicated firewall service for a vlan by using the method SoftLayer_Product_Order::placeOrder.
First we'll build a skeleton of SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated
object, providing the Vlan's ID.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the package id, quantity, and vlan id for the Firewall you wish to order
	quantity    := 1
	packageId   := 0
	vlanId      := 1174279

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItemPrices method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(2390) },         // Hardware Firewall (Dedicated)
	}

	// Build a skeleton SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated
	// object containing the order you wish to place.
	templateObject := datatypes.Container_Product_Order_Network_Protection_Firewall_Dedicated {
		Container_Product_Order : datatypes.Container_Product_Order {
			Prices    : prices,
			PackageId : sl.Int(packageId),
			Quantity  : sl.Int(quantity),
		},
    		VlanId : sl.Int(vlanId),
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
