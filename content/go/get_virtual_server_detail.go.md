---
title: "get_virtual_server_detail.go"
description: "get_virtual_server_detail.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware_Server"
tags:
    - "virtualservers"
---


```go
/*
Get Virtual Guest details.

Retrieve virtual server information and print a report with server hostname, domain, ip addresses,
cpu, ram, operating system, etc.
This script makes a single call to the getObject() method in the SoftLayer_Virtual_Guest service
and uses an object mask to retrieve related information.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/article/object-Masks

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
	apikey 	 := "set me"

	// The id of bare metal server you wish to get its details 320760
	guestId := 29857155

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Hardware_Server service
	service := services.GetVirtualGuestService(sess)

	// The object-mask needed to get BMS information
	mask := "id;fullyQualifiedDomainName;hostname;domain;primaryIpAddress;datacenter.longName;" +
		"status.name;provisionDate;primaryBackendIpAddress;maxMemory;startCpus;maxCpu;" +
		"maxCpuUnits;lastOperatingSystemReload.modifyDate;lastTransaction.transactionGroup.name;" +
		"operatingSystem.softwareDescription.longDescription"

	// Call to getObject() method
	server, err := service.Id(guestId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get server object:\n - %s\n", err)
		return
	}

	// Following code prints the BMS information
	format := "%-18s %-35v %-22s %-30s\n"
	fmt.Printf("\nBARE METAL SERVER (%d)\n\n", *server.Id)
	fmt.Printf(format,"NAME: ",*server.FullyQualifiedDomainName,
		"LOCATION:",*server.Datacenter.LongName)
	fmt.Printf(format,"HOSTNAME: ",*server.Hostname,
		"PUBLIC IP:",*server.PrimaryIpAddress)
	fmt.Printf(format,"DOMAIN: ",*server.Domain,
		"PRIVATE IP:",*server.PrimaryBackendIpAddress)

	// If OS was reloaded get the date
	var reloadDate = ""
	if server.LastOperatingSystemReload != nil {
		reloadDate = fmt.Sprint(server.LastOperatingSystemReload.ModifyDate)
	} else {
		reloadDate = "N/A"
	}

	// Print VSI configuration
	fmt.Printf("\nCONFIGURATION\n%s","-------------\n")
	fmt.Printf(format, "STATUS: ", *server.Status.Name,
		"LAST TRANSACTION #: ", *server.LastTransaction.TransactionGroup.Name)
	fmt.Printf(format, "START DATE: ", *server.ProvisionDate,
		"RELOADED #: ", reloadDate)

	// Before to print System information we need to concatenate data in order to show readable
	// information.
	operatingSystem := server.OperatingSystem.SoftwareDescription.LongDescription
	processor	:= fmt.Sprint(*server.MaxCpu, " ", *server.MaxCpuUnits)
	ramMemory   	:= fmt.Sprint(*server.MaxMemory, " MB")

	// Print VSI system
	fmt.Printf("\nSYSTEM\n%s","------\n")
	fmt.Printf(format, "OPERATING SYSTEM: ", *operatingSystem, "", "")
	fmt.Printf(format, "PROCESSOR: ", processor, "RAM: ",ramMemory)
}

```
