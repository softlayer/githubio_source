---
title: "cancel_server.go"
description: "cancel_server.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
/*
Cancel a bare metal server

This script looks for a server by hostname to cancel it. The server will be cancelled immediately if
it is billed Hourly, for Monthly server the cancellation will be made after next bill date.
To cancel the server we will call to cancelItem() method of SoftLayer_Billing_Item service since
cancelService() method cannot be used for Bare Metal Servers. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/editObject
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
https://sldn.softlayer.com/article/object-Masks
https://sldn.softlayer.com/article/object-filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/filter"
)

func main() {
	// SoftLayer API username and key
	username   := "set me"
	apikey     := "set me"

	// The hostname of server you wish to cancel.
	serverName := "set me"

	// In order to cancel billing item of server we need to set following values
	cancelAssociatedBillingItems := false
	reason := "No longer needed"
	customerNote := "BMS - canceled"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account, SoftLayer_Hardware_Server, and SoftLayer_Billing_Item services
	accountService  := services.GetAccountService(sess)
	hardwareService := services.GetHardwareServerService(sess)
	billingService  := services.GetBillingItemService(sess)

	// Following filter and mask helps to get the ID of bare metal server
	filter := filter.Build(filter.Path("hardware.hostname").Eq(serverName))
	mask   := "id;hostname;hourlyBillingFlag"

	// Call the getHardware() method to get list of servers that matches with the filter
	hardware, err := accountService.Mask(mask).Filter(filter).GetHardware()
	if err != nil {
		fmt.Printf("\n Unable to find server '" + serverName + "'\n - %s\n", err)
		return
	}

	// If server name was not found we throw a message
	if len(hardware) < 1 {
		fmt.Printf("\n Unable to find server '%s'\n", serverName)
	} else {
		// Get the SoftLayer_Billing_Item by calling the method getBillingItem() of service
		// SoftLayer_Hardware_Server
		billingItem, err := hardwareService.Id(*hardware[0].Id).GetBillingItem()
		if err != nil {
			fmt.Printf("\n Unable to get the billing item of server \n - %s\n", err)
			return
		}

		// If server is billed hourly it will be cancelled immediately, for monthly server
		// the cancellation will be made after next bill date.
		cancelImmediately := hardware[0].HourlyBillingFlag

		// Call the cancelItem() method in order to cancel the bare metal server
		result, err := billingService.Id(*billingItem.Id).CancelItem( cancelImmediately,
			&cancelAssociatedBillingItems, &reason, &customerNote )
		if err != nil {
			fmt.Printf("\n Unable to cancel the server '" + serverName + "'\n - %s\n", err)
			return
		}

		// Print final result
		if result {
			fmt.Printf("\n Server '%s' was successfuly cancelled\n", serverName)
		} else {
			fmt.Printf("\n Server '%s' could not be cancelled\n", serverName)
		}
	}
}

```
