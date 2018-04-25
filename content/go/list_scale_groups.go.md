---
title: "list_scale_groups.go"
description: "list_scale_groups.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
/*
Get all Scale Groups from account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getScaleGroups
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group
https://sldn.softlayer.com/article/object-Masks

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

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Declare mask that will be used to get more information about regional groups
	mask := "id,balancedTerminationFlag,cooldown,minimumMemberCount,maximumMemberCount,name,status,regionalGroupId,suspendedFlag,terminationPolicyId,virtualGuestMembers[id,virtualGuest[id,domain,hostname,maxCpu,maxMemory,status]]"

	// Call method getScaleGroups() method in order to retrieve all scale groups.
	scaleGroups, err := service.Mask(mask).GetScaleGroups()
	if err != nil {
		fmt.Printf("\n Unable to get scale groups from account:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, group := range scaleGroups{
		// Following helps to print the result in json format.
		jsonFormat, jsonErr := json.Marshal(group)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
