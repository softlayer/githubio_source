---
title: "get_gateway_details.go"
description: "get_gateway_details.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
/*
Get Network Gateway details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getPossibleInsideVlans
http://sldn.softlayer.com/article/object-masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of gateway you wish to get its information
	gatewayId := 244163

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Gateway service
	service := services.GetNetworkGatewayService(sess)

	// Set mask to get specific gateway's details.
	mask := "status.name;publicIpAddress.ipAddress;privateIpAddress.ipAddress;publicIpv6Address.ipAddress;" +
		"publicVlan[id;vlanNumber;primaryRouter.hostname;networkSpace];" +
		"privateVlan[id;vlanNumber;primaryRouter.hostname;networkSpace];" +
		"members[priority;hardware[id;fullyQualifiedDomainName;primaryIpAddress;" +
		"primaryBackendIpAddress;primaryNetworkComponent.primaryVersion6IpAddressRecord.ipAddress;" +
		"operatingSystem[id;passwords[username;password]]]];insideVlans[id;bypassFlag;" +
		"networkVlan[id;vlanNumber;primaryRouter.hostname;networkSpace]]"

	// Call to getObject() method in order to get Gateway's data
	gateway, err := service.Id(gatewayId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get gateway object:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(gateway, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
