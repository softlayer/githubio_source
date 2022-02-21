---
title: "get_subnets.go"
description: "get_subnets.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```go
/*
Retrieve the subnets for a VLAN

Retrieve all the subnets for a determinate VLAN associated with a SoftLayer customer account
We do this with a call to the getSubnets() method in the SoftLayer_Network_Vlan API service.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets

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

	// Vlan id you wish to get its subnets
	vlanId := 1054267

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Vlan service
	service := services.GetNetworkVlanService(sess)

	// Object-Mask to get specific subnet's information
	mask := "id;networkIdentifier;cidr;subnetType;totalIpAddresses;usableIpAddressCount"

	// Call to getSubnets() in order to retrieve all vlan's subnets.
	subnets, err := service.Id(vlanId).Mask(mask).GetSubnets()
	if err != nil {
		fmt.Printf("\n Unable to get Vlan's subnets:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,subnet := range subnets {
		jsonFormat, jsonErr := json.Marshal(subnet)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
