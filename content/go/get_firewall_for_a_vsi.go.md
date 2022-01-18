---
title: "get_firewall_for_a_vsi.go"
description: "get_firewall_for_a_vsi.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "firewalls"
---


```go
/*
Get the firewall associated to a VSI.

On this case we'll first retrieve the Virtual Guest ID by using the method Virtual_Guest::findByIpAddress,
and finally we'll use the method Virtual_Guest::getFirewallServiceComponent in order to get the firewall
component of VSI. See bellow for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getFirewallServiceComponent

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

	// The Ip Address used by a VSI
	ipAddress := "159.8.52.188"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest service
	service := services.GetVirtualGuestService(sess)

	// Call findByIpAddress() method in order to retrieve the VSI
	vsi, err := service.FindByIpAddress(&ipAddress)
	if err != nil {
		fmt.Printf("\n Unable to find VSI's through Ip Address:\n - %s\n", err)
		return
	} 

	// Call getFirewallServiceComponent() method in order to retrieve the Firewall from VSI
	firewall, err := service.Id(*vsi.Id).GetFirewallServiceComponent()
	if err != nil {
		fmt.Printf("\n Unable to get firewall component from VSI:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(firewall,"","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
