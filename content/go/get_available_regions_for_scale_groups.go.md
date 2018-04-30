---
title: "get_available_regions_for_scale_groups.go"
description: "get_available_regions_for_scale_groups.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location_Group"
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
/*
Get the regional groups available for use by scaling groups. This also includes datacenter
children that are available.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/getAvailableRegionalGroups
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group
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

	// Get SoftLayer_Scale_Group service
	service := services.GetScaleGroupService(sess)

	// Declare mask that will be used to get more information about regional groups
	mask := "id,name,description,locationGroupTypeId,locationGroupType,locations"

	// Call method getAvailableRegionalGroups()
	regionalGroups, err := service.Mask(mask).GetAvailableRegionalGroups()
	if err != nil {
		fmt.Printf("\n Unable to get available regional groups:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, region := range regionalGroups{
		// Following helps to print the result in json format.
		jsonFormat, jsonErr := json.Marshal(region)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
