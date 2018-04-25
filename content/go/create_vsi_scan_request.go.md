---
title: "create_vsi_scan_request.go"
description: "create_vsi_scan_request.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "vulnerabilityscan"
---


```
/*
Create a Vulnerability Scan Request for a SoftLayer_Virtual_Guest.

This example shows how to create a scan request for a SoftLayer_Virtual_Guest object. First, we'll
retrieve data like accountId, guestId and ipAddress to build a object template and pass it to
SoftLayer_Network_Security_Scanner_Request::createObject method in order to create the scan request.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
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

	// The id of virtual guest you wish to create a scan request
	guestId := 31003555

	// Create a session
	sess := session.New(username, apikey)

	// Get Account, Virtual_Guest, and Network_Security_Scanner_Request services
	accountService      := services.GetAccountService(sess)
	virtualGuestService := services.GetVirtualGuestService(sess)
	scanRequestService  := services.GetNetworkSecurityScannerRequestService(sess)

	// Get SoftLayer_Account object
	account, err := accountService.GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get Account object:\n - %s\n", err)
		return
	}

	// Following mask helps to get the id and ip addresses from virtual guest.
	guestMask := "id;primaryIpAddress;primaryBackendIpAddress"

	// Call to SoftLayer_Virtual_Guest::getObject in order to get id and ip addresses.
	guest, err := virtualGuestService.Id(guestId).Mask(guestMask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get Virtual Guest object:\n - %s\n", err)
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
		AccountId: sl.Int(*account.Id),
		GuestId:   sl.Int(*guest.Id),
		IpAddress: sl.String(*guest.PrimaryIpAddress),
	}

	// Object-Mask in order to get specific data from response.
	scanMask := "accountId;createDate;id;ipAddress;guestId;status[name]"

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
