---
title: "get_all_scan_requests.go"
description: "get_all_scan_requests.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "vulnerabilityscan"
---


```
/*
Get all Vulnerabilities Scan Requests from SoftLayer_Account.

This example shows how to get all scan request from SoftLayer_Account. On this case we'll filter
the response in order to get Pending or Processing requests (all uncompleted).
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSecurityScanRequests
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Security_Scanner_Request
https://sldn.softlayer.com/article/object-filters
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	/*
	You can filter using the following status:
		- Scan Pending
		- Scan Processing
		- Scan Complete
		- Scan Cancelled
		- Generating Report.
	Following filter is to get all uncompleted scan requests in the Account
	*/
	filter := filter.Path("securityScanRequests.status.name").NotEq("Scan Complete").Build()

	// Object-Mask in order to get specific data
	mask := "createDate;id;ipAddress;guestId;hardwareId;status[name]"

	// Use getSecurityScanRequests() method to get all scan requests from Account.
	scanRequests, err := service.Filter(filter).Mask(mask).GetSecurityScanRequests()
	if err != nil {
		fmt.Printf("\n Unable to get the scan requests:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,scan := range scanRequests {
		jsonFormat, jsonErr := json.Marshal(scan)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
