---
title: "create_virtual_guest.go"
description: "create_virtual_guest.go"
date: "2018-04-25"
classes: 
    - "SoftLayer_Container_Product_Order_Virtual_Guest"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "virtualservers"
---


```
/*
Order a new Virtual Guest

Build a SoftLayer_Container_Product_Order_Virtual_Guest object for a new virtual server order and
pass it to the SoftLayer_Product_Order API service to order it.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order

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
  	username    := ""
  	apikey      := "apikey_goes_here"

	// Declare the hostname, domain, location, packageId and quantity for the virtual
	// server you wish to order
  	quantity    := 1
  	hostname    := "test-template"
  	domain      := "example.com"
  	location    := "DALLAS05"
  	packageId   := 46

	// Build a skeleton SoftLayer_Virtual_Guest object to model the hostname and domain of
	// virtual server. If you set quantity greater than 1 then you need to define hostname/domain
	// per virtual server you wish to order.
  	virtualGuests := []datatypes.Virtual_Guest {
    		{	// Hostname and domain of SoftLayer_Virtual_Guest object
      			Hostname : sl.String(hostname),
      			Domain   : sl.String(domain),
    		},
	}

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
  	prices := []datatypes.Product_Item_Price {
    		{ Id: sl.Int( 1640) },     // 1 x 2.0 GHz Core
    		{ Id: sl.Int( 1644) },     // 1 GB RAM
    		{ Id: sl.Int(  905) },     // Reboot / Remote Console
    		{ Id: sl.Int(  272) },     // 10 Mbps Public & Private Networks
    		{ Id: sl.Int(50231) },     // 1000 GB Bandwidth
    		{ Id: sl.Int(   21) },     // 1 IP Address
    		{ Id: sl.Int( 2202) },     // 25 GB (SAN)
    		{ Id: sl.Int(13945) },     // CentOS 6.x - Minimal Install (64 bit)
    		{ Id: sl.Int(   55) },     // Host Ping Monitoring
    		{ Id: sl.Int(   57) },     // Email and Ticket Notifications
    		{ Id: sl.Int(   58) },     // Automated Notification Response
    		{ Id: sl.Int(  420) },     // Unlimited SSL VPN Users & 1 PPTP VPN User per account
    		{ Id: sl.Int(  418) },     // Nessus Vulnerability Assessment & Reporting
    		{ Id: sl.Int(   22) },     // 4 Public IP Addresses
  	}


	// Build a Container_Product_Order object containing the order you wish to place.
	orderTemplate := datatypes.Container_Product_Order {
		ComplexType   : sl.String("SoftLayer_Container_Product_Order_Virtual_Guest"),
		Quantity      : sl.Int(quantity),
		VirtualGuests : virtualGuests,
		Location      : sl.String(location),
		PackageId     : sl.Int(packageId),
		Prices        : prices,
	}

	/*
 	You can also build the SoftLayer_Container_Product_Order object as follows:

	orderTemplate := datatypes.Container_Product_Order_Virtual_Guest{
		Container_Product_Order_Hardware_Server: datatypes.Container_Product_Order_Hardware_Server{
			Container_Product_Order: datatypes.Container_Product_Order{
				Quantity      : sl.Int(quantity),
				VirtualGuests : virtualGuests,
				Location      : sl.String(location),
				PackageId     : sl.Int(packageId),
				Prices        : prices,
			},
		},
	}
	*/

	// Create a session
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
