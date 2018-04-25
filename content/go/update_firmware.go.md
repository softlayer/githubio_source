---
title: "update_firmware.go"
description: "update_firmware.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
/*
Update the firmware in a Bare Metal server

The script makes a single call to SoftLayer_Hardware_Server::createFirmwareUpdateTransaction
method to update the firmware in a bare metal server.
See below for more details

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/createFirmwareUpdateTransaction

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of bare metal server you wish to update the firmware
	hardwareId := 438878

	// Firmware update parameters.
	// Set with "1" to update and "0" to skip
	ipmi 		:= 1
	raidController  := 1
	bios 		:= 1
	harddrive 	:= 0

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Hardware_Server service
	service := services.GetHardwareServerService(sess)

	// Update the firmware by using the createFirmwareUpdateTransaction() method
	// It will bring your server offline for approximately 20 minutes while the updates
	// are in progress.
	result, err := service.Id(hardwareId).CreateFirmwareUpdateTransaction(&ipmi,&raidController,&bios,&harddrive)
	if err != nil {
		fmt.Printf("\n Unable to update the firmware:\n - %s\n", err)
		return
	}

	fmt.Print(result)
}

```
