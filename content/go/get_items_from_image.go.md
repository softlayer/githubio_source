---
title: "get_items_from_image.go"
description: "get_items_from_image.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Item"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "package"
---


```
/*
Get items from an image template

This script returns an array of SoftLayer_Product_Item objects which are part of a
SoftLayer_Virtual_Guest_Block_Device_Template_Group object

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemsFromImageTemplate
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/

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
	username := "set me"
	apikey   := "set me"

	// The id of package you wish to get information
	packageId := 46             // Virtual Server Instance

	// Declare the image template id
	imageTemplateId := 1370911

	// Build a SoftLayer_VIrtual_Guest_Block_Device_Template_Group object
	imageTemplate := datatypes.Virtual_Guest_Block_Device_Template_Group{
		Id: sl.Int(imageTemplateId),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Package service
	service := services.GetProductPackageService(sess)

	// Call the getItemsFromImageTemplate() method.
	items, err := service.Id(packageId).GetItemsFromImageTemplate(&imageTemplate)
	if err != nil {
		fmt.Printf("\n Unable to get items from image template:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,item := range items {
		jsonFormat, jsonErr := json.Marshal(item)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
