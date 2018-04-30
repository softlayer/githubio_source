---
title: "get_vlan_details.go"
description: "get_vlan_details.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
/*
Retrieve VLAN details such as router hostname, vlanNumber, primary router and subnet.

Retrieve the vlan's information by calling to the getObject() method in the SoftLayer_Network_Vlan
API service, and we using an object mask to retrieve associated subnets and primary router records.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject

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

	// Vlan id you wish to get its details
	vlanId := 1054267

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Vlan service
	service := services.GetNetworkVlanService(sess)

	// Object-Mask to get specific vlan's information
	mask := "id;name;vlanNumber;primaryRouter[id;hostname];subnets[id;ipAddresses[id;ipAddress]]"

	// Call to getObject() in order to retrieve vlan's details.
	vlan, err := service.Id(vlanId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get Vlan's information:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(vlan,"","    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
