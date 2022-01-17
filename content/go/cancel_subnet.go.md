---
title: "cancel_subnet.go"
description: "cancel_subnet.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Billing_Item"
tags:
    - "subnets"
---


```go
/*
Cancel a Subnet. Cancel network subnet using its billing Item.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of Subnet you wish to get information about "Allowed Network Storages".
	subnetId := 259934

	// In order to cancel billing item of subnet we need to set following values
	cancelImmediately     := true
	cancelAssociatedItems := true
	reason                := "For testing purposes"
	customerNote          := "API test"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Subnet and SoftLayer_Billing_Item services
	subnetService := services.GetNetworkSubnetService(sess)
	billingService := services.GetBillingItemService(sess)

	// Get the billing item from Subnet
	billingItem, err := subnetService.Id(subnetId).GetBillingItem()
	if err != nil {
		fmt.Printf("\n Unable to get IP Addresses from Subnet:\n - %s\n", err)
		return
	}

	// Call th method SoftLayer_Billing_Item::cancelItem in order to cancel the Subnet service.
	// You can also use cancelService() instead of cancelItem() method to cancel immediately
	// without filling a reason or note.
	result, err := billingService.Id(*billingItem.Id).CancelItem(&cancelImmediately, &cancelAssociatedItems, &reason, &customerNote)
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	fmt.Println(result)
}

```
