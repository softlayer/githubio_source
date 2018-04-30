---
title: "create_server_simplified.go"
description: "create_server_simplified.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware"
tags:
    - "virtualservers"
---


```
/*
Create a Virtual Guest server using the simplified way.

This example shows how customers can get a new virtual guest server by using the method
SoftLayer_Virtual_Guest::createObject which is a simplified way to create a server.
Take account that servers created via createObject() will incur charges on your account. For testing
input parameters we'll use the SoftLayer_Virtual_Guest::generateOrderTemplate method.
See below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCreateObjectOptions
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username  := "set me"
	apikey    := "set me"

	// To get the configuration options call the method getCreateObjectOptions() of
	// SoftLayer_Virtual_Guest service. e.g.:
	//	createOptions = virtualGuestService.GetCreateObjectOptions()
	// Following is an example to create a template with the configuration options
	// that we want.
	templateObject := datatypes.Virtual_Guest{
		Hostname:   sl.String("softlayer"),				// Name of server
		Domain:     sl.String("example.com"),				// Domain of server
		StartCpus:  sl.Int(2),						// The number of logical CPU cores to allocate
		MaxMemory:  sl.Int(4),						// The amount of memory to allocate in gigabytes.
		Datacenter: &datatypes.Location{				// Specifies on which data center will be provisioned the server.
			Name: sl.String("ams01"),				// Amsterdam
		},
		OperatingSystemReferenceCode: sl.String("UBUNTU_16_64"),	// OS: Ubuntu Linux 16.04 LTS Xenial Xerus Minimal Install (64 bit)
		HourlyBillingFlag: sl.Bool(false),				// Specifies the billing type for the server (Monthly).
		LocalDiskFlag: 	   sl.Bool(false),				// Set true for LOCAL disk, otherwise SAN disks will be provisioned.
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Hardware service
	service := services.GetVirtualGuestService(sess)

	// Use generateOrderTemplate() method to check for errors. Replace this with createObject()
	// when you are ready to create the bare metal server.
	receipt, err := service.GenerateOrderTemplate(&templateObject)
	if err != nil {
		fmt.Printf("\n Unable to create the Virtual Guest Server:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","   ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
