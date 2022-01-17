---
title: "bypass_vlans.go"
description: "bypass_vlans.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```go
/*
Bypass the vlans in a gateway device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/bypassVlans
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/filter"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of gateway
	gatewayId := 61522

	// The ids of Vlans you wish to bypass
	vlanIds := []int {865555,1084325}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Gateway service
	service := services.GetNetworkGatewayService(sess)

	// To get the Vlan objects we might use the SoftLayer_Network_Vlan::getObject for each one
	// and build an array in order to pass it to bypassVlans() method. But take account that
	// Vlans should be inside gateway and to get a vlans' array we can use following code.
	filter := filter.Path("insideVlans").In("networkVlanId").Opt("name",vlanIds).Build()

	// Call method getInsideVlans() method to get a vlans's array according to the filter
	gatewayVlans, err := service.Id(gatewayId).Filter(filter).GetInsideVlans()
	if err != nil {
		fmt.Printf("\n Unable to get gateway inside vlans:\n - %s\n", err)
		return
	}

	// Call method bypassVlans() in order to bypass all vlans into array
	bypassErr := service.Id(gatewayId).BypassVlans(gatewayVlans)
	if bypassErr != nil {
		fmt.Printf("\n Unable to bypass selected vlans:\n - %s\n", bypassErr)
		return
	}

	fmt.Println("\n Selected Vlans were bypassed!!")
}

```
