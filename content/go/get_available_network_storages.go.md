---
title: "get_available_network_storages.go"
description: "get_available_network_storages.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Storage"
tags:
    - "subnets"
---


```go
/*
Retrieve the list of available SoftLayer_Network_Storage volumes that can be authorized
to a SoftLayer_Network_Subnet object. To do this we'll use the method getAvailableNetworkStorages().
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getAvailableNetworkStorages
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Storage

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

	// The id of Subnet you wish to get information about available network storages.
	subnetId := 22545

	// Declare what NAS type of storages you wish to get, it can be either 'ISCSI',
	// 'NAS', or '*' for both
	nasType := "*"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Subnet service
	service := services.GetNetworkSubnetService(sess)

	// Call the method getAvailableNetworkStorages()
	availableStorages, err := service.Id(subnetId).GetAvailableNetworkStorages(&nasType)
	if err != nil {
		fmt.Printf("\n Unable to get available network storages:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, storage := range availableStorages {
		jsonFormat, jsonErr := json.Marshal(storage)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
