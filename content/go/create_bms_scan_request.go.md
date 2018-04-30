---
title: "create_bms_scan_request.go"
description: "create_bms_scan_request.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "vulnerabilityscan"
---


```
/*
Create a Vulnerability Scan Request for a SoftLayer_Hardware_Server.

This example shows how to create a scan request for a SoftLayer_Hardware_Server object. First, we'll
retrieve data like accountId, hardwareId and ipAddress to build a object template and pass it to
SoftLayer_Network_Security_Scanner_Request::createObject method in order to create the scan request.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Security_Scanner_Request
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of hardware server you wish to create a scan request
	hardwareId := 438878

	// Create a session
	sess := session.New(username, apikey)

	// Get Account, Hardware_Server, and Network_Security_Scanner_Request services
	accountService     := services.GetAccountService(sess)
	hardwareService    := services.GetHardwareServerService(sess)
	scanRequestService := services.GetNetworkSecurityScannerRequestService(sess)

	// Get SoftLayer_Account object
	account, err := accountService.GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get Account object:\n - %s\n", err)
		return
	}

	// Following mask helps to get the id and ip addresses from hardware server.
	hardwareMask := "id;primaryIpAddress;primaryBackendIpAddress"

	// Call to SoftLayer_Hardware_Server::getObject in order to get id and ip addresses.
	hardware, err := hardwareService.Id(hardwareId).Mask(hardwareMask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get Hardware Server object:\n - %s\n", err)
		return
	}

	/*
	Build the object template used to make a scan request. The Network_Security_Scanner_Request
	service can scan any Ip Address belonging to your account:
		- Primary Ip Address
		- Primary Backend Ip Address
		- Portable Ip Addresses
		- Static Secondary IPs
	If you have a firewall, SoftLayer's administrative networks need to be allowed for the
	vulnerability scan to be effective. If a firewall is blocking all ports, the report may not
	show any problems even if some exist.
	*/
	objectTemplate := datatypes.Network_Security_Scanner_Request{
		AccountId:  sl.Int(*account.Id),
		HardwareId: sl.Int(*hardware.Id),
		IpAddress:  sl.String(*hardware.PrimaryIpAddress),
	}

	// Object-Mask in order to get specific data from response.
	scanMask := "accountId;createDate;id;ipAddress;hardwareId;status[name]"

	// Call to createObject() method to create a scan request.
	scanRequest, err := scanRequestService.Mask(scanMask).CreateObject(&objectTemplate)
	if err != nil {
		fmt.Printf("\n Unable to create a scan request:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(scanRequest,"","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

```
