---
title: "place_order_monitoring.go"
description: "place_order_monitoring.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
tags:
    - "monitoring"
---


```
/*
Order a Monitoring Package

Build a SoftLayer_Container_Product_Order_Monitoring_Package object for a new monitoring order and
pass it to the SoftLayer_Product_Order service to order it. In this case we'll order a
Basic (Hardware and OS) package with Basic Monitoring Package - Linux configuration.
For more details see below.

Important manual pages:
https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Monitoring_Package
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group

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

	// Declare the packageId, sendQuoteEmailFlag and useHourlyPricing.
	packageId          := sl.Int(0)
	sendQuoteEmailFlag := sl.Bool(true)
	useHourlyPricing   := sl.Bool(true)

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(2302) },    // Monitoring Package - Basic
	}

	// Template ID for monitoring group (in this case Basic Monitoring package for Unix/Linux.)
	configurationTemplateGroups := []datatypes.Monitoring_Agent_Configuration_Template_Group{
		{ Id: sl.Int(3)},
	}

	// Declare on which Virtual Server you want to add the Monitoring Service.
	virtualGuests := []datatypes.Virtual_Guest{
		{Id: sl.Int(18382383)},
	}

	// Build a Container_Product_Order_Monitoring_Package object containing the order
	// you wish to place
	templateObject := datatypes.Container_Product_Order_Monitoring_Package {
		Container_Product_Order : datatypes.Container_Product_Order{
			PackageId	   : packageId,
			Prices        	   : prices,
			SendQuoteEmailFlag : sendQuoteEmailFlag,
			UseHourlyPricing   : useHourlyPricing,
			VirtualGuests	   : virtualGuests,
		},
		ConfigurationTemplateGroups: configurationTemplateGroups,
	}

	// Create a session
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
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
