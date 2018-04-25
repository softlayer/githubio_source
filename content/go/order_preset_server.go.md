---
title: "order_preset_server.go"
description: "order_preset_server.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
/*
Order a new server with preset configuration.

The presets used to simplify ordering by eliminating the need for price ids when submitting orders.
Also when the order contains a preset id, it is not possible to configure VLANs in the order.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey	 := "set me"

	// Declare the hostname, domain, location, packageId and quantity for the
	// storage you wish to order
	quantity  := 1
	location  := "MEXICO"
	packageId := 200		// Bare Metal Servers
	presetId  := 97			// Dual Xeon 2620, 64GB Ram, 2x1TB SATA disks, Non-RAID
	hostname  := "softlayer"
	domain    := "example.com"

	// Build a skeleton SoftLayer_Hardware_Server object to model the hostname and domain
	// of server. If you set quantity greater than 1 then you need to define hostname/domain
	// per server you wish to order.
	hardware := []datatypes.Hardware{
		{
			Hostname: sl.String(hostname),
			Domain:   sl.String(domain),
		},
	}

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(13942) },	// CentOS 6.x (64 bit)
		{ Id: sl.Int(50261) },	// 20000 GB Bandwidth
		{ Id: sl.Int(  273) },	// 100 Mbps Public & Private Network Uplinks
		{ Id: sl.Int(  420) },	// Unlimited SSL VPN Users & 1 PPTP VPN User per account
		{ Id: sl.Int(   21) },	// 1 IP Addresses
		{ Id: sl.Int(  906) },	// Reboot / KVM over IP
	}

	// Build a skeleton SoftLayer_Container_Product_Order object containing
	// the order you wish to place.
	orderTemplate := datatypes.Container_Product_Order{
		Quantity:	sl.Int(quantity),
		Location:	sl.String(location),
		PackageId:	sl.Int(packageId),
		PresetId: 	sl.Int(presetId),
		Prices:		prices,
		Hardware:  	hardware,
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
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
