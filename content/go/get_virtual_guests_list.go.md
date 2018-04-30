---
title: "get_virtual_guests_list.go"
description: "get_virtual_guests_list.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
tags:
    - "virtualservers"
---


```
/*
List Virtual servers in the Account

This script gets all Virtual servers of Account, on this case we'll use the getVirtualGuests()
method of SoftLayer_Account service.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package service
	service := services.GetAccountService(sess)

	// mask
	mask := "id;hostname;domain;primaryIpAddress;primaryBackendIpAddress;datacenter"

	// Call the getActivePresets() method.
	hardware, err := service.Mask(mask).GetVirtualGuests()
	if err != nil {
		fmt.Printf("\n Unable to get Virtual Servers:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,server := range hardware {
		jsonFormat, jsonErr := json.Marshal(server)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}

}

```
