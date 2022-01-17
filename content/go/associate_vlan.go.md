---
title: "associate_vlan.go"
description: "associate_vlan.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---


```go
/*
Associate a Network_Vlan object in a gateway device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/createObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway_Vlan

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

	// If true, Vlan will be bypassed. If false, it will be routed.
	bypassFlag := true

	// The id of gateway you wish to associate.
	gatewayId := 61522

	// The id of vlan you wish to associate. To get the vlan id you can run the method
	// SoftLayer_Network_Gateway_Vlan::getPossibleInsideVlans
	vlanId := 1502997

	// Build Network_Gateway_Vlan skeleton in order to pass it to createObject() method
	templateObject := datatypes.Network_Gateway_Vlan{
		BypassFlag:       sl.Bool(bypassFlag),
		NetworkGatewayId: sl.Int(gatewayId),
		NetworkVlanId:    sl.Int(vlanId),
	}

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Gateway_Vlan service
	service := services.GetNetworkGatewayVlanService(sess)

	// Call to createObject() method to associate vlan to gateway
	gatewayVlan, err := service.CreateObject(&templateObject)
	if err != nil {
		fmt.Printf("\n Unable to create association:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(gatewayVlan,"","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
