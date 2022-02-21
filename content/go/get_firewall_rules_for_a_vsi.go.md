---
title: "get_firewall_rules_for_a_vsi.go"
description: "get_firewall_rules_for_a_vsi.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Component_Firewall"
tags:
    - "firewalls"
---


```go
/*
Get the associated Firewall's rules for a vsi.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Component_Firewall/GetRules

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
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

	// The id of Virtual server you wish to retrieve it firewall rules
  	vsiId := 33051333 //24589535

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest and SoftLayer_Network_Component_Firewall services
	guestService := services.GetVirtualGuestService(sess)
	firewallService := services.GetNetworkComponentFirewallService(sess)

	// Call to getFirewallServiceComponent() method to get the firewall object
	firewall, err := guestService.Id(vsiId).GetFirewallServiceComponent()
	if err != nil {
		fmt.Printf("\n Unable to get firewall component from VSI:\n - %s\n", err)
		return
	}

	// Call to getRules() method in order to retrieve all firewall rules.
	rules, err := firewallService.Id(*firewall.Id).GetRules()
	if err != nil {
		fmt.Printf("\n Unable to get firewall rules:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, rule := range rules {
		jsonFormat, jsonErr := json.Marshal(rule)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
