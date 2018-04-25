---
title: "cancel_cdn.go"
description: "cancel_cdn.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Billing_Item"
tags:
    - "cdn"
---


```
/*
Cancel CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/getBillingItem
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of CDN you wish to cancel
	cdnId := 90273

	// Declare cancelImmediately, cancelAssociatedItems, reason and customNote in order to pass
	// them to cancelItem() method.
	cancelImmediately := false
	cancelAssociated  := false
	cancelReason      := "A reason for cancelation"
	cancelNote        := "A custom note"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Billing_Item and SoftLayer_Network_ContentDelivery_Account services
	billingService := services.GetBillingItemService(sess)
	cdnService := services.GetNetworkContentDeliveryAccountService(sess)

	// Get the billing item of CDN object
	billingItem, err := cdnService.Id(cdnId).GetBillingItem()
	if err != nil {
		fmt.Printf("\n Unable to get the billing item from CDN object:\n - %s\n", err)
		return
	}

	// Cancel the CDN through its billing item, use CancelItem() method.
	result, err := billingService.Id(*billingItem.Id).CancelItem(&cancelImmediately,&cancelAssociated,&cancelReason,&cancelNote)
	if err != nil {
		fmt.Printf("\n Unable the billing item of CDN object:\n - %s\n", err)
		return
	}

	fmt.Println(result)
}

```
