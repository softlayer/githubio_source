---
title: "get_server_detail.go"
description: "get_server_detail.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```go
/*
Get Bare Metal details.

Retrieve bare metal information and print a report with server hostname, domain, ip addresses,
cpu, ram, operating system, etc.
This script makes a single call to the getObject() method in the SoftLayer_Hardware_Server service
and uses an object mask to retrieve related information.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
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
	apikey   := "set me"

	// The id of bare metal server you wish to get its details 320760
	hardwareId := 249142

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Hardware_Server service
	service := services.GetHardwareServerService(sess)

	// The object-mask needed to get BMS information
	mask := "id;fullyQualifiedDomainName;hostname;domain;primaryIpAddress;primaryBackendIpAddress;" +
		"hardwareStatus.status;provisionDate;serialNumber;manufacturerSerialNumber;motherboard;" +
		"lastOperatingSystemReload.modifyDate;lastTransaction.transactionGroup.name;memoryCount;" +
		"memory;datacenter.longName;processors;operatingSystem.softwareDescription.longDescription"

	// Call to getObject() method
	hardware, err := service.Id(hardwareId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get server object:\n - %s\n", err)
		return
	}

	// Following code prints the BMS information
	format := "%-18s %-35v %-22s %-30s\n"
	fmt.Printf("\nBARE METAL SERVER (%d)\n\n", *hardware.Id)
	fmt.Printf(format,"NAME: ",*hardware.FullyQualifiedDomainName,
		"LOCATION:",*hardware.Datacenter.LongName)
	fmt.Printf(format,"HOSTNAME: ",*hardware.Hostname,
		"PUBLIC IP:",*hardware.PrimaryIpAddress)
	fmt.Printf(format,"DOMAIN: ",*hardware.Domain,
		"PRIVATE IP:",*hardware.PrimaryBackendIpAddress)

	// If OS was reloaded get the date
	var reloadDate = ""
	if hardware.LastOperatingSystemReload != nil {
		reloadDate = fmt.Sprint(hardware.LastOperatingSystemReload.ModifyDate)
	} else {
		reloadDate = "N/A"
	}

	// Print BMS configuration
	fmt.Printf("\nCONFIGURATION\n%s","-------------\n")
	fmt.Printf(format, "STATUS: ", *hardware.HardwareStatus.Status,
		"LAST TRANSACTION #: ", *hardware.LastTransaction.TransactionGroup.Name)
	fmt.Printf(format, "START DATE: ", *hardware.ProvisionDate,
		"SERIAL #: ", *hardware.SerialNumber)
	fmt.Printf(format, "RELOADED: ", reloadDate,
		"MFR SERIAL #: ", *hardware.ManufacturerSerialNumber)

	// Before to print System information we need to concatenate data in order to show readable
	// information.
	processorModel   := hardware.Processors[0].HardwareComponentModel
	motherboardModel := hardware.Motherboard.HardwareComponentModel
	ramMemoryModel   := hardware.Memory[0].HardwareComponentModel

	operatingSystem := hardware.OperatingSystem.SoftwareDescription.LongDescription
	processor	:= fmt.Sprint(*processorModel.Capacity, "GHz ", *processorModel.Name)
	motherboard 	:= fmt.Sprint(*motherboardModel.Manufacturer, " ", *motherboardModel.Name)
	ramMemory   	:= fmt.Sprint(*hardware.MemoryCount, "x", *ramMemoryModel.Capacity, "GB ",
				*ramMemoryModel.Manufacturer, " ", *ramMemoryModel.Name)

	// Print BMS system
	fmt.Printf("\nSYSTEM\n%s","------\n")
	fmt.Printf(format, "MOTHERBOARD: ", motherboard, "PROCESSOR: ", processor)
	fmt.Printf(format, "RAM: ", ramMemory, "OPERATING SYSTEM: ", *operatingSystem)
}

```
