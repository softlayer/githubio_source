---
title: "list_global_ips.go"
description: "list_global_ips.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet_IpAddress_Global"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Subnet_IpAddress"
tags:
    - "globalips"
---


```go
/*
List global IP address

This example lists all global IP address from an account. On this case we'll make a single call to
SoftLayer_Account::getGlobalIpRecords method. See below for more details.

Important manual pages:
http://sldn.softlayer.com/article/python
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getGlobalIpRecords
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Global
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// mask
	mask := "destinationIpAddress;ipAddress"

	// Call the getGlobalIpRecords() method.
	ipRecords, err := service.Mask(mask).GetGlobalIpRecords()
	if err != nil {
		fmt.Printf("\n Unable to get Global IP address:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,record := range ipRecords {
		jsonFormat, jsonErr := json.Marshal(record)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```
