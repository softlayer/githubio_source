---
title: "edit_scale_group.go"
description: "edit_scale_group.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```go
/*
Edit Scale Group

Following parameters can be edited:
  - name
  - cooldown
  - minimumMemberCount
  - maximumMemberCount
  - terminationPolicyId
Take account that group's status must be active to set those fields.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/datatypes"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of scale group you wish to edit
	scaleGroupId := 1226695

	// Build the skeleton of SoftLayer_Scale_Group object with the new data
	objectTemplate := datatypes.Scale_Group{
		Name: sl.String("Scale Group Test Name"),
		MinimumMemberCount: sl.Int(0),
		MaximumMemberCount: sl.Int(5),
		Cooldown: sl.Int(1800),
		TerminationPolicyId: sl.Int(1),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Scale_Group service
	service := services.GetScaleGroupService(sess)

	// Call to editObject() method in order to edit the Scale Group
	result, err := service.Id(scaleGroupId).EditObject(&objectTemplate)
	if err != nil {
		fmt.Printf("\n Unable to edit the scale group:\n - %s\n", err)
		return
	}

  	fmt.Println(result)
}

```
