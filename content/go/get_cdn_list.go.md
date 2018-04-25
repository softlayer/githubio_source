---
title: "get_cdn_list.go"
description: "get_cdn_list.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
/*
List all CDN in the Account

This script gets all SoftLayer_Network_ContentDelivery_Account objects from Account, on this case
we'll make a simple call to getCdnAccounts() method of SoftLayer_Account service.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getCdnAccounts
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Declare object mask in order to get specific CDN data
	mask := "id;cdnAccountName;createDate;legacyCdnFlag;providerPortalAccessFlag;status[id;name]"

	// Call the getCdnAccounts() method.
	cdnList, err := service.Mask(mask).GetCdnAccounts()
	if err != nil {
		fmt.Printf("\n Unable to retrieve CDN objects:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,cdn := range cdnList {
		jsonFormat, jsonErr := json.Marshal(cdn)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```
