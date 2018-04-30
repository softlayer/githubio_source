---
title: "list_vlans_dedicated_firewalls.go"
description: "list_vlans_dedicated_firewalls.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Vlan"
tags:
    - "firewalls"
---


```
/*
List Vlans that have dedicated firewalls in the account

This script will display a list of network Vlan objects with their firewall configuration. On this
example we'll call to SoftLayer_Account::getNetworkVlans method with a filter in order to get all
Network Vlans with "dedicatedFirewallFlag" as true.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
https://sldn.softlayer.com/article/object-filters
https://sldn.softlayer.com/article/object-Mask

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
  	"encoding/json"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Declare the filter that will be used to find Vlans with dedicated firewall
	filter := filter.Path("networkVlans.dedicatedFirewallFlag").Eq(1).Build()

	// Declare object-mask in order to retrieve specific data
	mask := "dedicatedFirewallFlag,primaryRouter,subnets,firewallNetworkComponents,firewallInterfaces,networkVlanFirewall"

	// Call to SoftLayer_Account::getNetworkVlans method to retrieve vlans according to filter.
	vlans, err := service.Mask(mask).Filter(filter).GetNetworkVlans()
	if err != nil {
		fmt.Printf("\n Unable to get Vlan with dedicated firewall:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, vlan := range vlans {
		jsonFormat, jsonErr := json.Marshal(vlan)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
