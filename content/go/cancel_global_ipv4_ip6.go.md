---
title: "cancel_global_ipv4_ip6.go"
description: "cancel_global_ipv4_ip6.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress_Global"
    - "SoftLayer_Billing_Item"
tags:
    - "globalips"
---


```go
/*
Cancel Global Ip Address

This example shows how to cancel a Global IP Address.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress_Global/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
https://sldn.softlayer.com/article/object-Masks

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

	// The id  of Global IP Address you wish to cancel.
	globalIpId := 61823

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Subnet_IpAddress_Global and SoftLayer_Billing_Item services
	globalIpService  := services.GetNetworkSubnetIpAddressGlobalService(sess)
	billingService  := services.GetBillingItemService(sess)

	// Declare mask used to get the id of billing item
	mask := "id;billingItem[id]"

	// Call to getObject() method in order to get global ip data according to mask
	globalIp, err := globalIpService.Id(globalIpId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get the Global Ip Address\n - %s\n", err)
		return
	}

	// Call to Billing_Item::cancelService method to cancel the Global Ip Address
	result, err := billingService.Id(*globalIp.BillingItem.Id).CancelService()
	if err != nil {
		fmt.Printf("\n Unable to cancel Global Ip Address\n - %s\n", err)
		return
	}

	// Print final result
	if result {
		fmt.Printf("\n Global Ip Address '%d' was successfuly cancelled\n", globalIpId)
	} else {
		fmt.Printf("\n Global Ip Address '%d' could not be cancelled\n", globalIpId)
	}
}

```
