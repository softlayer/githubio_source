---
title: "get_scan_report.go"
description: "get_scan_report.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Security_Scanner_Request"
tags:
    - "vulnerabilityscan"
---


```
/*
Get report of an specific scan request.

On this case we'll use the method getReport() from SoftLayer_Network_Security_Scanner_Request
service. The method will return a HTML string.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request/getReport

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

	// The id of scan request you want to get its report.
	scanId := 2066403

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Security_Scanner_Request service
	service := services.GetNetworkSecurityScannerRequestService(sess)

	// Use getReport() method to get specific information in HTML format
	report, err := service.Id(scanId).GetReport()
	if err != nil {
		fmt.Printf("\n Unable to get the scan's report:\n - %s\n", err)
		return
	}

	fmt.Print(report)
}

```
