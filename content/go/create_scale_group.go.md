---
title: "create_scale_group.go"
description: "create_scale_group.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Network_Component"
    - "SoftLayer_Scale_Group"
tags:
    - "scalegroups"
---


```go
/*
Create Scale Group

This example shows how to create a SoftLayer_Scale_Group object, to do this we will build a
skeleton of SoftLayer_Scale_Group with a SoftLayer_Virtual_Guest object.
Please see below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Scale_Group/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Scale_Group
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest

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
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare location as following
	location := &datatypes.Location {Name : sl.String("hkg02")}

	// Declare array of SoftLayer_Virtual_Guest_Network_Component objects
	networkComponents := []datatypes.Virtual_Guest_Network_Component {
		{ MaxSpeed : sl.Int(100)},
	}

	// Build the SoftLayer_Virtual_Guest object that will be added to the Scale_Group
	virtualGuest := datatypes.Virtual_Guest {
		Domain                       : sl.String("example.com"),
		Hostname                     : sl.String("test-template"),
		PostInstallScriptUri         : sl.String("https://www.softlayer.com/script"),
		StartCpus                    : sl.Int(1),
		HourlyBillingFlag            : sl.Bool(true),
		LocalDiskFlag                : sl.Bool(true),
		OperatingSystemReferenceCode : sl.String("CENTOS_LATEST"),
		MaxMemory                    : sl.Int(1),
		PrivateNetworkOnlyFlag       : sl.Bool(false),
		Datacenter                   : location,
		NetworkComponents            : networkComponents,
	}

	// Build the skeleton of SoftLayer_Scale_Group object that will be used to create the
	// Scale Group
	objectTemplate := datatypes.Scale_Group{
		Cooldown                   : sl.Int(1800),
		MaximumMemberCount         : sl.Int(5),
		MinimumMemberCount         : sl.Int(1),
		Name                       : sl.String("New Scale Group"),
		RegionalGroupId            : sl.Int(102),
		SuspendedFlag              : sl.Bool(false),
		TerminationPolicyId        : sl.Int(1),
		VirtualGuestMemberTemplate : &virtualGuest,
		VirtualGuestMemberCount    : sl.Uint(uint(0)),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Scale_Group service
	service := services.GetScaleGroupService(sess)

	// Call to createObject() method in order to create the Scale Group
	scaleGroup, err := service.CreateObject(&objectTemplate)
	if err != nil {
		fmt.Printf("\n Unable to create a Scale Group:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(scaleGroup, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
