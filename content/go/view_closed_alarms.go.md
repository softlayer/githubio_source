---
title: "view_closed_alarms.go"
description: "view_closed_alarms.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "monitoring"
---


```
/*
View closed alarms of an advanced monitoring.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getMonitoringClosedAlarms

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"encoding/json"
	"github.com/softlayer/softlayer-go/sl"
	"time"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of virtual server you want to get it closed alarms
	guestId  := 26165877

	startDate, _ := time.Parse("2006-01-02 15:04:05 -0700 UTC", "2012-01-01 23:02:03 +0000 UTC")

	endDate, _ := time.Parse("2006-01-02 15:04:05 -0700 UTC", "2017-05-30 23:02:03 +0000 UTC")

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest service
	virtualService := services.GetVirtualGuestService(sess)

	// Retrieve all closed alarms of virtual guest
	activeAlarms, err := virtualService.Id(guestId).GetMonitoringClosedAlarms(sl.Time(startDate), sl.Time(endDate))
	if err != nil {
		fmt.Printf("\n Unable to get closed alarms\n - %s\n", err)
		return
	}

	// Following helps to print results in JSON format
	for _, alarm := range activeAlarms{
		jsonFormat, jsonErr := json.Marshal(alarm)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
