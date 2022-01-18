---
title: "view_agent_status.go"
description: "view_agent_status.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```go
/*
Get the status of the monitoring agents in a Virtual Guest.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
http://sldn.softlayer.com/article/object-masks

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

	// The id of virtual server you want to get its agents
	guestId  := 33051333

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest service
	virtualService := services.GetVirtualGuestService(sess)

	// Declare object-mask which will be used to get monitoring agents
	mask := "id,monitoringRobot[id,robotStatus[name]],monitoringAgents[statusName,name,id]," +
		"monitoringServiceEligibilityFlag,datacenter"

	// Retrieve Virtual Guest in order to get its monitoring agents
	guest, err := virtualService.Id(guestId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get Virtual Guest\n - %s\n", err)
		return
	}

	// Following helps to print results in JSON format
	jsonFormat, jsonErr := json.MarshalIndent(guest, "", "    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
