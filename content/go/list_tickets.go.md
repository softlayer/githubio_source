---
title: "list_tickets.go"
description: "list_tickets.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Brand"
    - "SoftLayer_Notification_Occurrence_Event"
tags:
    - "brands"
---


```go
/*
List tickets.

The script retrieves all the tickets in a brand account.
It displays the same result like in https://agent.softlayer.com/support/ticket/list

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Notification_Occurrence_Event/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Notification_Occurrence_Event
http://sldn.softlayer.com/article/Object-Filters
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
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

	// The id of Brand you wish to retrieve his agents
	brandId := 2

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Brand service
	service := services.GetBrandService(sess)

	// Declare filter which will be used to retrieve only assigned and open tickets
	filter := filter.Path("tickets.status.name").In("Open","Assigned").Build()

	// Declare object-mask in order to get specific information of ticket
	mask := "group[name],status[name],statusId,id,createDate,title,assignedUser[username]," +
		"attachedFileCount,totalUpdateCount,modifyDate,lastEditType,newUpdatesFlag," +
		"attachedHardwareCount,account[companyName,accountStatus[name]],state[stateType]," +
		"priority,scheduledActions[transactionGroup,ticketScheduledActionReference]," +
		"attachedVirtualGuestCount,assignedAgents[username]"

	// Retrieve all Open and Assigned tickets
	accounts, err := service.Id(brandId).Mask(mask).Filter(filter).GetTickets()
	if err != nil {
		fmt.Printf("\n Unable to retrieve tickets - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, account := range accounts {
		jsonFormat, jsonErr := json.Marshal(account)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
