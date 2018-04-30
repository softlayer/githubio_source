---
title: "restart_agent.go"
description: "restart_agent.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```
/*
Restart an agent.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/restartMonitoringAgent
http://sldn.softlayer.com/article/object-masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/datatypes"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of virtual server
	guestId  := 33051333

	// Agent name you want to restart
	agentName := "Process Monitoring Agent"

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest and SoftLayer_Monitoring_Agent services
	virtualService := services.GetVirtualGuestService(sess)
	monitoringService := services.GetMonitoringAgentService(sess)

	// Declare object-mask which will be used to get monitoring agents
	mask := "id,monitoringAgents[statusName,name,id]"

	// Retrieve Virtual Guest in order to get its monitoring agents
	guest, err := virtualService.Id(guestId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get Virtual Guest\n - %s\n", err)
		return
	}

	// Declare an empty variable that will be used to store the agent
	monitoringAgent := datatypes.Monitoring_Agent{}

	// Search agent by its name
	for _, agent := range guest.MonitoringAgents{
		if *agent.Name == agentName {
			monitoringAgent = agent
		}
	}

	// Return message if agent doesn't exists
	if monitoringAgent.Id == nil {
		fmt.Printf("\n The VSI does not have the monitor agent: - %s\n", agentName)
		return
	}

	// Restart the monitoring agent
	result, err := monitoringService.Id(*monitoringAgent.Id).RestartMonitoringAgent()
	if err != nil {
		fmt.Printf("\n Unable to get restart the agent\n - %s\n", err)
		return
	}

	fmt.Println(result)
}

```
