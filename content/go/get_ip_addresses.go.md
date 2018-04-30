---
title: "get_ip_addresses.go"
description: "get_ip_addresses.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Subnet"
tags:
    - "subnets"
---


```
/*
Retrieve all the ip addresses associated with a subnet.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getIpAddresses
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
https://sldn.softlayer.com/article/object-Masks

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

	// The id of Subnet you wish to get information about its ipAddress
	subnetId := 22545

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Subnet service
	service := services.GetNetworkSubnetService(sess)

	// Declare the object mask used to get specific data from subnet
	mask := "id;ipAddress;isBroadcast;isGateway;isNetwork;isReserved"

	// Call to method getIpAddresses() in order to get the ip address from subnet
	ipAddresses, err := service.Id(subnetId).Mask(mask).GetIpAddresses()
	if err != nil {
		fmt.Printf("\n Unable to get IP Addresses from Subnet:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, ipAddress := range ipAddresses {
		jsonFormat, jsonErr := json.Marshal(ipAddress)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
