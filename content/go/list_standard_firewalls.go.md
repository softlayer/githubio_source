---
title: "list_standard_firewalls.go"
description: "list_standard_firewalls.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "firewalls"
---


```go
/*
List standard firewalls

This script will display a list of Virtual Servers that have a firewall configuration. On this
example we'll call to SoftLayer_Account::getVirtualGuests method with a filter in order to get all
servers with "firewallServiceComponent".

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
https://sldn.softlayer.com/article/object-filters
https://sldn.softlayer.com/article/object-Mask

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
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

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Declare the filter that will be used to find Virtual Guests with firewall
	filter := filter.Path("virtualGuests.firewallServiceComponent").NotNull().Build()

	// Declare object-mask in order to retrieve specific data
	mask := "id;hostname;domain;firewallServiceComponent"

	// Call to SoftLayer_Account::getVirtualGuests method to retrieve virtual servers
	// according to filter.
	servers, err := service.Mask(mask).Filter(filter).GetVirtualGuests()
	if err != nil {
		fmt.Printf("\n Unable to get virtual servers with firewall:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, guest := range servers {
		jsonFormat, jsonErr := json.Marshal(guest)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
