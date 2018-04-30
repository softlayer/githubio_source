---
title: "get_bandwidth_data.go"
description: "get_bandwidth_data.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
/*
Get bandwidth data in a CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthData

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
	"time"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of CDN Account you wish to get bandwidth data information
	cdnId := 8166

	// Declare between what dates you wish to get the bandwidth data. On this case, we'll
	// retrieve data between 2016-01-01 and 2017-05-10
	startDate, _ := time.Parse("2006-01-02","2016-01-01")
	endDate, _   := time.Parse("2006-01-02","2017-05-10")

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_ContentDelivery_Account service
	service := services.GetNetworkContentDeliveryAccountService(sess)

	// Call the getBandwidthData() method to get mapping information.
	bandwidth, err := service.Id(cdnId).GetBandwidthData(sl.Time(startDate), sl.Time(endDate))
	if err != nil {
		fmt.Printf("\n Unable to retrieve pull mapping information of CDN:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,data := range bandwidth {
		jsonFormat, jsonErr := json.Marshal(data)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```
