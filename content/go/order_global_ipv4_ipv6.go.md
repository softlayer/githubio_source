---
title: "order_global_ipv4_ipv6.go"
description: "order_global_ipv4_ipv6.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Network_Subnet"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Order"
tags:
    - "globalips"
---


```go
/*
Order a new Global IPv4/IPv6

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet

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

	// Declare the complexType, packageId and quantity
  	complexType := "SoftLayer_Container_Product_Order_Network_Subnet"
  	quantity    := 1
  	packageId   := 0

	// Create a session.
  	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package and SoftLayer_Product_Order services
  	productPackageService := services.GetProductPackageService(sess)
  	productOrderService := services.GetProductOrderService(sess)

	// Following filter helps to get item prices for GLOBAL_IPV6 IP Address
	// Change GLOBAL_IPV6 by GLOBAL_IPV4 if you want to order an Ip Address v4
  	filter := `{"itemPrices":{"item":{"keyName":{"operation":"GLOBAL_IPV6"}}}}`

	// Get SoftLayer_Product_Item_Price objects for Ip Address
	itemPrices, err := productPackageService.Id(packageId).Filter(filter).GetItemPrices()
	if err != nil {
		fmt.Printf("\n Unable to Item Prices:\n - %s\n", err)
		return
	}

	// As we only need one item price for Ip Address, we will build an array of
	// SoftLayer_Product_Item_Price objects by adding its id.
  	prices := []datatypes.Product_Item_Price {
    		{ Id: sl.Int(*itemPrices[0].Id) },
  	}

	// Build the Container_Product_Order object containing the order you wish to place
	templateObject := datatypes.Container_Product_Order {
    		ComplexType   : sl.String(complexType),
    		Quantity      : sl.Int(quantity),
    		PackageId     : sl.Int(packageId),
    		Prices        : prices,
	}

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := productOrderService.VerifyOrder(&templateObject)
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
