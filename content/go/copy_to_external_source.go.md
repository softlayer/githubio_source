---
title: "copy_to_external_source.go"
description: "copy_to_external_source.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "image-templates"
---


```go
/*
Copy to external source

This script creates a transaction to export/copy a template to an external source.
Flex Images cannot be copied to external sources.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToExternalSource
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration

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
)

func main() {
	// SoftLayer API username and key.
	username  := "set me"
	apikey    := "set me"

	// The image id you wish to copy to external source. Take account that Flex Images are not
	// supported.
	imageId := 879951

	// Declare storage, cluster, container and filename used to create the URL where image
	// will be copied.
	storageName   := "SLOS307608-40"
	clusterName   := "sao01"
	containerName := "softlayer_container"
	fileName      := "centos6test.vhd"

	// Create URL where image will be copied
	swift := fmt.Sprintf("swift://%s@%s/%s/%s", storageName, clusterName, containerName, fileName )

	// Build the Container_Virtual_Guest_Block_Device_Template_Configuration object
	configuration := datatypes.Container_Virtual_Guest_Block_Device_Template_Configuration{
		Uri: sl.String(swift),
	}

	// Create session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest_Block_Device_Template_Group service.
	service := services.GetVirtualGuestBlockDeviceTemplateGroupService(sess)

	// Copy the standard image to an external source.
	result, err := service.Id(imageId).CopyToExternalSource(&configuration)
	if err != nil {
		fmt.Printf("\n Unable to copy image to external source:\n - %s\n", err)
		return
	} 

	// Print result
	fmt.Println(result)
}

```
