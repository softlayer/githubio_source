---
title: "order_vyatta_gateway.go"
description: "order_vyatta_gateway.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "gateway"
---


```go
/*
Order a Network Gateway Appliance (Vyatta)

The script orders a Network Gateway (Vyatta), it uses the SoftLayer_Product_Order::placeOrder
to make the order.
See below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance
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
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the hostname, domain, location, packageId and quantity for the
	// gateway you wish to order
	quantity  := 1
	location  := "AMSTERDAM"
	packageId := 174
	hostname  := "softlayer"
	domain    := "example.com"

	// Build a skeleton SoftLayer_Hardware object to model the hostname and domain
	// of server. If you set quantity greater than 1 then you need to define hostname/domain
	// per server you wish to order.
	hardware := []datatypes.Hardware {
		{
			Hostname: sl.String(hostname),
			Domain:   sl.String(domain),
		},
	}

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(76965) },	// RAM 8 GB DDR3 1333
		{ Id: sl.Int(74865) },	// Single Intel Xeon E3-1270 (4 Cores, 3.40 GHz)
		{ Id: sl.Int(36044) },	// Vyatta 6.x Subscription Edition (64 bit)
		{ Id: sl.Int(17129) },	// 1 IPv6 Address
		{ Id: sl.Int( 1267) },	// 500 GB SATA
		{ Id: sl.Int(  906) },	// Reboot / KVM over IP
		{ Id: sl.Int(  876) },	// Non-RAID
		{ Id: sl.Int(  420) },	// Unlimited SSL VPN Users & 1 PPTP VPN User per account
		{ Id: sl.Int(  418) },	// Nessus Vulnerability Assessment & Reporting
		{ Id: sl.Int(  342) },	// Single Intel Xeon E3-1270 (4 Cores, 3.40 GHz)
		{ Id: sl.Int(  273) },	// 100 Mbps Public & Private Network Uplinks
		{ Id: sl.Int(   58) },	// Automated Notification
		{ Id: sl.Int(   57) },	// Email and Ticket
		{ Id: sl.Int(   55) },	// 500 GB SATA
		{ Id: sl.Int(   21) },	// 1 IP Addresses
	}

	// Build a skeleton Container_Product_Order_Hardware_Server_Gateway_Appliance object
	// containing the order you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Hardware_Server_Gateway_Appliance{}
	orderTemplate.OrderContainers = []datatypes.Container_Product_Order{
		{
			Quantity:  sl.Int(quantity),
			Location:  sl.String(location),
			PackageId: sl.Int(packageId),
			Prices:    prices,
			Hardware:  hardware,
		},
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
