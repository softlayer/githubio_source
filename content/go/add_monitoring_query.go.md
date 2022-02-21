---
title: "add_monitoring_query.go"
description: "add_monitoring_query.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```go
/*
The script creates a monitoring network with Service ping in a determinate IP address

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/datatypes"
	"encoding/json"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {

	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The ID of virtual guest to want to apply monitoring query.
	guestId  := 32834621

	// The IP address to be monitored. Must be attached to the hardware/virtual guest
	// on this object.
	ipAddress := "10.77.176.12"

	// The ID of the query type to use. You can get the ID types using the following method.
	// SoftLayer_Network_Monitor_Version1_Query_Host_Stratum::getAllQueryTypes
	queryTypeId := 17       // SLOW PING

	// The ID of the response action to take when the monitor fails. You can get IDs using
	// following method SoftLayer_Network_Monitor_Version1_Query_Host_Stratum::getAllResponseTypes
	responseActionId := 1           // No Nothing

	// The status of this monitoring instance. Anything other than "ON" means that the monitor
	// has been disabled
	status := "ON"

	// The number of 5-minute cycles to wait before the "responseAction" is taken.
	// If set to 0, the response action will be taken immediately
	waitCycles := 1

	// Build object template used to create the network monitor
	objectTemplate := datatypes.Network_Monitor_Version1_Query_Host{
		GuestId		 : sl.Int(guestId),
		IpAddress	 : sl.String(ipAddress),
		QueryTypeId	 : sl.Int(queryTypeId),
		ResponseActionId : sl.Int(responseActionId),
		Status		 : sl.String(status),
		WaitCycles	 : sl.Int(waitCycles),
	}

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Monitor_Version1_Query_Host service
	service := services.GetNetworkMonitorVersion1QueryHostService(sess)

	// Declare mask used to get specific information from monitor.
	mask := "queryType[id,name]"

	// Create network monitoring query
	monitor, err := service.Mask(mask).CreateObject(&objectTemplate)
	if err != nil {
		fmt.Printf("\n Unable to add network monitor:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(monitor, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
