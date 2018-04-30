---
title: "cancel_vlan.go"
description: "cancel_vlan.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
/*
Cancel a SoftLayer_Network_VLan.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_VLan/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_VLan
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService

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

	// The Network_Vlan id you wish to cancel
	vlanId := 1281697

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Vlan and SoftLayer_Billing_Item services
	vlanService    := services.GetNetworkVlanService(sess)
	billingService := services.GetBillingItemService(sess)

	// Use masks in order to retrieve the billing item id
	mask := "id"

	// Get the SoftLayer_Network_Vlan object
	billingItem, err := vlanService.Id(vlanId).Mask(mask).GetBillingItem()
	if err != nil {
		fmt.Printf("\n Unable to get the billing item of Network Vlan:\n - %s\n", err)
		return
	}

	// Cancel the SoftLayer_Billing_Item of Vlan.
	result, err := billingService.Id(*billingItem.Id).CancelService()
	if err != nil {
		fmt.Printf("\n Unable to cancel service of Network Vlan:\n - %s\n", err)
		return
	}

	fmt.Println(result)
}

```
