---
title: "get_scan_requests.go"
description: "get_scan_requests.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "vulnerabilityscan"
---


```go
/*
Get Vulnerabilities Scan Requests from a Virtual Guest.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getSecurityScanRequests
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
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of virtual guest you want to know the scan requests
	guestId := 31003555

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest service
	service := services.GetVirtualGuestService(sess)

	// Object-Mask in order to get specific data
	mask := "accountId;createDate;id;ipAddress;status[name]"

	// Use getSecurityScanRequests() method to get all scan requests from VSI.
	scanRequests, err := service.Id(guestId).Mask(mask).GetSecurityScanRequests()
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
