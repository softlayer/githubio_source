---
title: "disassociate_vlan.go"
description: "disassociate_vlan.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---


```
/*
Remove association between Vlan and Gateway device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/deleteObject
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

	// The id of gateway you wish to remove the association.
	gatewayId := 61522

	// The id of vlan you wish to remove the association. This should be associated to the
	// gateway above. You can execute the method SoftLayer_Network_Gateway_Vlan::getInsideVlans
	// to verify it.
	vlanId := 1502997

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Gateway and SoftLayer_Network_Gateway_Vlan services
	gatewayService := services.GetNetworkGatewayService(sess)
	gatewayVlanService := services.GetNetworkGatewayVlanService(sess)

	// Use filter to get the Network_Gateway_Vlan object
	filter := filter.Path("insideVlans").In("networkVlanId").Eq(vlanId).Build()

	// Call method getInsideVlans() method to get the Network_Gateway_Vlan object
	gatewayVlans, err := gatewayService.Id(gatewayId).Filter(filter).GetInsideVlans()
	if err != nil {
		fmt.Printf("\n Unable to get inside vlans:\n - %s\n", err)
		return
	}

	// Call to deleteObject() method to remove the association
	deleteErr := gatewayVlanService.Id(*gatewayVlans[0].Id).DeleteObject()
	if deleteErr != nil {
		fmt.Printf("\n Unable to remove association:\n - %s\n", deleteErr)
		return
	}

	fmt.Println("\n Selected Vlan was removed from association !!")
}

```
