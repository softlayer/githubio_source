---
title: "delete_monitoring_query.go"
description: "delete_monitoring_query.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```go
/*
Delete network monitoring

The script makes a single call to SoftLayer_Network_Monitor_Version1_Query_Host::deleteObject
method to delete the network monitoring for more information see below

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host/deleteObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/filter"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of virtual server you want to delete a monitor
	guestId  := 32834621

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest and SoftLayer_Network_Monitor_Version1_Query_Host services
	virtualService := services.GetVirtualGuestService(sess)
	monitorService := services.GetNetworkMonitorVersion1QueryHostService(sess)

	// Declare filter that will be used to retrieve specific monitoring objects
	filter := filter.Path("networkMonitors.queryType.name").Eq("SLOW PING").Build()

	// Get all Network Monitors according to filter
	monitoringItems, err := virtualService.Id(guestId).Filter(filter).GetNetworkMonitors()
	if err != nil {
		fmt.Printf("\n Unable to get network monitors:\n - %s\n", err)
		return
	}

	// Delete all monitors with type "SLOW PING"
	for _, monitor := range monitoringItems{
		monitorService, err := monitorService.Id(*monitor.Id).DeleteObject()
		if err != nil {
			fmt.Printf("\n Unable to delete network monitor:\n - %s\n", err)
			return
		}
		fmt.Println(monitorService)
	}
}

```
