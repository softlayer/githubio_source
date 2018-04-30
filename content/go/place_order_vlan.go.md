---
title: "place_order_vlan.go"
description: "place_order_vlan.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_Vlan"
tags:
    - "vlans"
---


```
/*
Example to create a new VLAN.

The script uses the placeOrder method to order a new VLAN with 32 static IP address

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
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

	// Declare the properties like complexType, location, packageId and quantity for the
	// vlan you wish to order
  	quantity           := 1
  	packageId          := 0
  	sendQuoteEmailFlag := true
	location           := "AMSTERDAM"
  	name               := "new-tested-vlan"
  	routerId           := 117960

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
  	itemPrices := []datatypes.Product_Item_Price {
    		{ Id: sl.Int(2018) },     // Price for the new Public Network Vlan
    		{ Id: sl.Int(1092) },     // Price for 32 Static Public IP Addresses
  	}

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Build the Container_Product_Order_Network_Vlan containing the order you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_Vlan {
    		Container_Product_Order : datatypes.Container_Product_Order {
			Prices		   : itemPrices,
			PackageId	   : sl.Int(packageId),
			Location	   : sl.String(location),
			Quantity	   : sl.Int(quantity),
			SendQuoteEmailFlag : sl.Bool(sendQuoteEmailFlag),
		},
    		Name	 : sl.String(name),
    		RouterId : sl.Int(routerId),
	}

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt,"","    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
