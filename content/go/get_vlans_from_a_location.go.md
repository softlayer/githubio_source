---
title: "get_vlans_from_a_location.go"
description: "get_vlans_from_a_location.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
/*
Retrieves vlans from specific location.

This example shows how the get all VLans located in 'Seoul 1', for that we'll use the method
getNetworkVlans() of Softlayer_Account service.
See below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
http://sldn.softlayer.com/article/object-Masks
http://sldn.softlayer.com/article/object-filters

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

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Object-Mask to get specific Vlan's information
	mask := "id;vlanNumber;primaryRouter;networkSpace"

	// Object-Filter to get all Vlans located in 'Seoul 1'
	filter := `{"networkVlans":{
			"primaryRouter":{
				"datacenter":{
					"longName":{"operation":"Seoul 1"}
				}
			}
		   }}`

  	// Call to getNetworkVlans in order to retrieve vlans according to filter.
	vlans, err := service.Mask(mask).Filter(filter).GetNetworkVlans()
	if err != nil {
		fmt.Printf("\n Unable to get Network Vlans:\n - %s\n", err)
		return
	}

	// Following loops help to print information about vlans
	fmt.Println("PRIMARY NETWORK COMPONENT")
	for _,vlan := range vlans {
		if *vlan.NetworkSpace == "PUBLIC" {
			fmt.Printf("Id: %d\tVlan Number: %d\tPrimary Router: %s\n",
				*vlan.Id, *vlan.VlanNumber, *vlan.PrimaryRouter.Hostname)
		}
	}

	fmt.Println("PRIMARY BACKEND NETWORK COMPONENT")
	for _,vlan := range vlans {
		if *vlan.NetworkSpace == "PRIVATE" {
			fmt.Printf("Id: %d\tVlan Number: %d\tPrimary Router: %s\n",
				*vlan.Id, *vlan.VlanNumber, *vlan.PrimaryRouter.Hostname)
		}
	}
}

```
