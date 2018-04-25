---
title: "edit_server.go"
description: "edit_server.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
/*
Edit a bare metal server's basic information

Change the 'notes' property for a single bare metal server by using the editObject() method of
SoftLayer_Hardware_Server service. On this case, we'll search the bare metal server by hostname
to know its id before to change its notes. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
https://sldn.softlayer.com/article/object-Masks
https://sldn.softlayer.com/article/object-filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username   := "set me"
	apikey     := "set me"

	// The hostname of server you wish to edit.
	serverName := "set me"

	// Define the new local properties to set. While we're only editing a server's notes
	// in this example you can also use editObject() to edit the server's hostname and domain.
	objectTemplate := datatypes.Hardware_Server{}
	objectTemplate.Notes = sl.String("This is my bare metal server!")

	/*
	You can also build the objectTemplate as follows:

	objectTemplate := datatypes.Hardware_Server{
		Hardware : datatypes.Hardware{
			Notes: sl.String("This is my bare metal server!"),
		},
	}
	*/

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account and SoftLayer_Hardware_Server services
	accountService  := services.GetAccountService(sess)
	hardwareService := services.GetHardwareServerService(sess)

	// Following filter and mask helps to get the ID of bare metal server
	filter := filter.Build(filter.Path("hardware.hostname").Eq(serverName))
	mask   := "id;hostname"

	// Call the getHardware() method to get list of hardware that matches with the filter
	hardware, err := accountService.Mask(mask).Filter(filter).GetHardware()
	if err != nil {
		fmt.Printf("\n Unable to find server '" + serverName + "'\n - %s\n", err)
		return
	}

	// If server name was not found we throw a message
	if len(hardware) < 1 {
		fmt.Printf("\n Unable to find server '%s'\n", serverName)
	} else {
		// Call the editObject() method in order to made changes in the server
		result, err := hardwareService.Id(*hardware[0].Id).EditObject(&objectTemplate)
		if err != nil {
			fmt.Printf("\n Unable to edit the server '" + serverName + "'\n - %s\n", err)
			return
		}

		// Print final result
		if result {
			fmt.Printf("\n Server '%s' was successfuly edited\n", serverName)
		} else {
			fmt.Printf("\n Server '%s' could not be edited\n", serverName)
		}
	}
}

```
