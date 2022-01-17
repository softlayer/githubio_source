---
title: "get_active_presets.go"
description: "get_active_presets.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Package_Preset"
tags:
    - "package"
---


```go
/*
Get active presets prices

This script retrieves the available preset configurations for this package, also
it provides information about the prices and items from them.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getActivePresets
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Preset
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

	// The id of package you wish to get information
	packageId := 200

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package service
	service := services.GetProductPackageService(sess)

	// Declare object mask in order to get specific data
	mask := "prices[item]"

	// Call the getActivePresets() method.
	activePresets, err := service.Id(packageId).Mask(mask).GetActivePresets()
	if err != nil {
		fmt.Printf("\n Unable to get active presets:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,preset := range activePresets {
		jsonFormat, jsonErr := json.Marshal(preset)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
