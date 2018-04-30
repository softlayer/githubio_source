---
title: "get_allowed_network_storage.go"
description: "get_allowed_network_storage.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Storage"
tags:
    - "subnets"
---


```
/*
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Network_Subnet has access to.
On this case we'll use the method SoftLayer_Network_Subnet::getAllowedNetworkStorage in order to
get all storage object that a subnet has access.
Please see below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getAllowedNetworkStorage
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

	// The id of Subnet you wish to get information about "Allowed Network Storages".
	subnetId := 551692

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Subnet service
	service := services.GetNetworkSubnetService(sess)

	// Call the method getAvailableNetworkStorages()
	allowedStorages, err := service.Id(subnetId).GetAllowedNetworkStorage()
	if err != nil {
		fmt.Printf("\n Unable to get allowed network storages:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, storage := range allowedStorages {
		jsonFormat, jsonErr := json.Marshal(storage)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
