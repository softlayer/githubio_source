---
title: "order_portable_private_subnet.go"
description: "order_portable_private_subnet.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
---


```
/*
Order a new portable private subnet.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
  	"encoding/json"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the quantity, location, and packageId for the subnet you wish to order.
	quantity  := 1
	packageId := 0
	location  := "DALLAS05"

	// The id of a Private Network Vlan. To get the list of vlans use the method
	// SoftLayer_Account::getPrivateNetworkVlans
	vlanId    := 865555

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(13981)},         // 4 Portable Private IP Addresses
	}

	// Build a skeleton Container_Product_Order_Network_Subnet object containing the order
	// you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_Subnet {
		Container_Product_Order : datatypes.Container_Product_Order {
			PackageId : sl.Int(packageId),
			Location  : sl.String(location),
			Quantity  : sl.Int(quantity),
			Prices    : prices,
		},
		EndPointVlanId : sl.Int(vlanId),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
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
