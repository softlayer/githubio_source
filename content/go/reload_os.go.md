---
title: "reload_os.go"
description: "reload_os.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Billing_Item"
tags:
    - "virtualservers"
---


```go
/*
Reload the Operating System of a Virtual Guest

This script reloads the Operating System configuration with another one. It makes a single call
to the reloadOperatingSystem() method in the SoftLayer_Virtual_Guest API service

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/reloadOperatingSystem

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey 	 := "set me"

	// The id of Virtual Guest server you wish to reload
	guestId := 29857155

	/*
	 The new items you want to load in the OS configuration. You can add following items:
	  - Operating System
	  - OS-Specific Addon
	  - CDP Addon
	  - Control Panel Software
	  - Database Software
	  - Anti-Virus & Spyware Protection
	  - Hardware & Software Firewall
	*/
	osDescriptions := [] string {
		"CentOS 6.x - Minimal Install (64 bit)",         // Operating System
		"APF Software Firewall for Linux",		 // Software Firewall for Linux OS
	}

	// Add an object mask to retrieve the prices related to the SoftLayer_Virtual_Guest object
	// for a list of the relational properties you can retrieve along with hardware.
	mask := "mask[billingItem[package[items[prices]]]]"

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetVirtualGuestService(sess)

	// Call to getObject() method in order to get the SoftLayer_Virtual_Guest object with
	// information set in the mask
	server, err := service.Id(guestId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get the Virtual Server:\n - %s\n", err)
		return
	}

	// Call to getActiveTransactions() to know if there are transactions in progress.
	transactions, err := service.Id(guestId).GetActiveTransactions()
	if err != nil {
		fmt.Printf("\n Unable to get Active Transactions:\n - %s\n", err)
		return
	}

	// Server can not be reloaded if there are pending_with_issues transactions.
	if len(transactions) > 0 {
		fmt.Print("\n Server can not be reloaded because there is a transaction in progress for this device.\n")
		return
	}

	// Server can not be reloaded if there isn't a SoftLayer_Billing_Item object.
	if server.BillingItem == nil {
		fmt.Print("\n Unable to continue with OS Reload. Please contact support.\n")
		return
	}

	// Following function (Function Literal) will get prices of items set in the
	// 'osDescriptions' variable.
	prices := func(descriptions []string, items []datatypes.Product_Item) []datatypes.Product_Item_Price {
		var itemPrices []datatypes.Product_Item_Price
		for _,itemDescription := range descriptions {
			for _,item := range items {
				if *item.Description == itemDescription {
					itemPrices = append(
						itemPrices,
						datatypes.Product_Item_Price { Id: sl.Int(*item.Prices[0].Id) },
					)
					break
				}
			}
		}
		return itemPrices
	}

	// Build the configuration skeleton that will be used to reload the OS
	configuration := datatypes.Container_Hardware_Server_Configuration{
		ItemPrices: prices(osDescriptions, server.BillingItem.Package.Items),
	}

	// Call method reloadOperatingSystem()
	reload, err := service.Id(*server.Id).ReloadOperatingSystem(sl.String("FORCE"), &configuration)
	if err != nil {
		fmt.Printf("\n Unable to reload the Operation System:\n - %s\n", err)
		return
	}

	fmt.Printf("\n %s - OS reload transaction is running with requested configuration\n", reload)
}

```
