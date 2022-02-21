---
title: "create_flex_image.go"
description: "create_flex_image.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Disk_Image_Capture_Template"
tags:
    - "image-templates"
---


```go
/*
Create an flex image from a Virtual Server

The script makes a single call to the  SoftLayer_Virtual_Guest::captureImage method to create a
flex image. Please see below for more information.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/captureImage
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key.
	username  := "set me"
	apikey    := "set me"

	// The virtual guest id you wish to create a flex image disk.
	virtualGuestId := 29857155

	// Build the template object that will be used to capture a flex image.
	captureTemplate := datatypes.Container_Disk_Image_Capture_Template {
		Description : sl.String("Description example"),
		Name        : sl.String("Image Name"),
		Summary     : sl.String("Summary example"),
	}

	// Create session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest service.
	service := services.GetVirtualGuestService(sess)

	// Capture flex image.
	flexImage, err := service.Id(virtualGuestId).CaptureImage(&captureTemplate)
	if err != nil {
		fmt.Printf("\n Unable to create Flex Image:\n - %s\n", err)
		return
	} 

	// Following creates a JSON object which is based on data of the captured image.
	jsonFormat, JsonErr := json.MarshalIndent(flexImage,"","     ")
	if JsonErr != nil {
		fmt.Println(JsonErr)
		return
	}

	// Print result in JSON format
	fmt.Println(string(jsonFormat))
}

```
