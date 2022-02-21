---
title: "activate_suspend_scale_group.go"
description: "activate_suspend_scale_group.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```go
/*
Activate or Suspend a scale group.

This example show how to ACTIVATE or SUSPEND the SoftLayer_Scale_Group object. For that we'll edit
the scale group by modifying the parameter 'suspendedFlag'.
Please see below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of scale group you wish to activate or suspend
	scaleGroupId := 1226695

	/*
	Build the skeleton of SoftLayer_Scale_Group object as following in order to modify the
	'suspendFlag' parameter.
	       TRUE   -    The scale group will be suspended.
	       FALSE  -    The scale group will be activated.
	*/
	objectTemplate := datatypes.Scale_Group {
		SuspendedFlag : sl.Bool(true),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Scale_Group service
	service := services.GetScaleGroupService(sess)

	// Call the method editObject() in order to activate or suspend the SoftLayer_Scale_Group
	result, err := service.Id(scaleGroupId).EditObject(&objectTemplate)
	if err != nil {
		fmt.Printf("\n Unable to activate or suspend the scale group:\n - %s\n", err)
		return
	} 

	fmt.Println(result)
}

```
