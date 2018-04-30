---
title: "get_firewall_ip_address.go"
description: "get_firewall_ip_address.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vlan"
tags:
    - "firewalls"
---


```
/*
Get the IP address from a VLan

The script lists the IP address of VLAN, it makes a single call to the method
SoftLayer_Network_Vlan::getFirewallProtectableIpAddresses.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getFirewallProtectableIpAddresses
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
  	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The Id of Vlan you wish to get its ip address
	vlanId := 494330

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Vlan service
	service := services.GetNetworkVlanService(sess)

	// Call to getFirewallProtectableIpAddresses() method in order to retrieve the Ip Address
	firewall, err := service.Id(vlanId).GetFirewallProtectableIpAddresses()
	if err != nil {
		fmt.Printf("\n Unable to get firewall:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(firewall, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
