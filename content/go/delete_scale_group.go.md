---
title: "delete_scale_group.go"
description: "delete_scale_group.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```
/*
Delete Scale Group

This can only be done on an empty, active group. This means that minimumMemberCount must be 0 since
it is the only way for a group to have no group members. To delete a group and all of its members
at the same time, use forceDeleteObject.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/deleteObject
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
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of scale group you wish to delete
	scaleGroupId := 1656275

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Scale_Group service
	service := services.GetScaleGroupService(sess)

	// Declare mask that will be used to get the minimumMemberCount data
	mask := "id;minimumMemberCount"

	// Call to getObject() method in order to get scale group's information.
	scaleGroup, err := service.Id(scaleGroupId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get the scale group:\n - %s\n", err)
		return
	}

	// Use 'deleteObject' the scale group when minimumMemberCount is 0, use 'forceDeleteForce'
	// when minimumMemberCount is 1 or more.
	if scaleGroup.MinimumMemberCount == sl.Int(0) {
		// Call to deleteObject() method in order to delete the scale group.
		result, err := service.Id(scaleGroupId).DeleteObject()
		if err != nil {
			fmt.Printf("\n Unable to delete the scale group:\n - %s\n", err)
			return
		}
		fmt.Println(result)
	} else {
		// Call to forceDeleteObject() method in order to delete the scale group with all
		// is members.
		result, err := service.Id(scaleGroupId).ForceDeleteObject()
		if err != nil {
			fmt.Printf("\n Unable to force delete the scale group:\n - %s\n", err)
			return
		}
		fmt.Println(result)
	}
}

```
