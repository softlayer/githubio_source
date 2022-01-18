---
title: "edit_virtual_guest.go"
description: "edit_virtual_guest.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualservers"
---


```go
/*
Edit a virtual guest server's basic information

Change the 'notes' and 'hostname' properties for a single virtual server by using the editObject()
method of SoftLayer_Virtual_Guest service. See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username  := "set me"
	apikey    := "set me"

	// The id of virtual guest you wish to edit.
	guestId := 29857155

	// Define the new local properties to set. While we're only editing a server's notes
	// in this example you can also use editObject() to edit the server's hostname and domain.
	objectTemplate := datatypes.Virtual_Guest{
		Hostname: sl.String("softlayer-guest"),
		Notes:    sl.String("This is my virtual server!"),
	}

	/*
	You can also build the objectTemplate as follows:

	objectTemplate := datatypes.Virtual_Guest{}
	objectTemplate.Hostname = sl.String("softlayer-hostname")
	objectTemplate.Notes    = sl.String("This is my virtual server!")
	*/

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest service
	virtualGuestService := services.GetVirtualGuestService(sess)

	// Call the editObject() method in order to made changes in the server
	result, err := virtualGuestService.Id(guestId).EditObject(&objectTemplate)
	if err != nil {
		fmt.Printf("\n Unable to edit the virtual guest server\n - %s\n", err)
		return
	}

	// Print final result
	if result {
		fmt.Println("\n Virtual Guest Server was successfuly edited")
	} else {
		fmt.Println("\n Virtual Guest Server could not be edited")
	}
}

```
