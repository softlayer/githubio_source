---
title: "get_network_monitors.go"
description: "get_network_monitors.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```
/*
Retrieve all network monitors of Virtual Guest.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest/getNetworkMonitors

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

	// Declare the packageId, quantity, sendQuoteEmailFlag and useHourlyPricing.
	guestId  := 32834621

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest service
	virtualService := services.GetVirtualGuestService(sess)

	// Declare mask used to get specific information from monitor.
	mask := "queryType[id,name]"

	// Retrieve all monitors in the virtual guest
	monitoringItems, err := virtualService.Id(guestId).Mask(mask).GetNetworkMonitors()
	if err != nil {
		fmt.Printf("\n Unable to get network monitors\n - %s\n", err)
		return
	}

	// Following helps to print results in JSON format
	for _, monitor := range monitoringItems{
		jsonFormat, jsonErr := json.Marshal(monitor)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
