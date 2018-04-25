---
title: "create_from_external_source.go"
description: "create_from_external_source.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "image-templates"
---


```
/*
Create Image Template from external source

This script creates a transaction to import a disk image from an external source and create
a standard image template

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group

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

	// Declare the name, note to be applied to the imported template
	name := "ExportImageTemplateTest"
	note := "Test - create from external source"

	/*
	Declare referenceCode of the operating system software description, some available options:
	   CENTOS_6_32, CENTOS_6_64, CENTOS_7_64, REDHAT_6_32, REDHAT_6_64, REDHAT_7_64, UBUNTU_12_32,
	   UBUNTU_12_64, UBUNTU_14_32, UBUNTU_14_64, WIN_2003-STD-SP2-5_32, WIN_2003-STD-SP2-5_64,
	   WIN_2008-STD-R2-SP1_64, WIN_2012-STD_64.
	*/
	operatingSystemReferenceCode := "CENTOS_6_64"

	// Declare storage, cluster, container and filename used to create the URL where image
	// will be copied.
	storageName   := "SLOS307608-40"
	clusterName   := "sao01"
	containerName := "softlayer_container"
	fileName      := "centos6test.vhd"

	// Build URL where image is hosted
	swift := fmt.Sprintf("swift://%s@%s/%s/%s", storageName, clusterName, containerName, fileName )

	// Build the Container_Virtual_Guest_Block_Device_Template_Configuration object
	configuration := datatypes.Container_Virtual_Guest_Block_Device_Template_Configuration{
		Name: sl.String(name),
		Note: sl.String(note),
		OperatingSystemReferenceCode: sl.String(operatingSystemReferenceCode),
		Uri: sl.String(swift),
	}

	// Create session
  	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest_Block_Device_Template_Group service.
  	service := services.GetVirtualGuestBlockDeviceTemplateGroupService(sess)

	// Create standard image from external source.
  	image, err := service.CreateFromExternalSource(&configuration)
	if err != nil {
		fmt.Printf("\n Unable to create standard image:\n - %s\n", err)
		return
	}

	// Following creates a JSON object which is based on data of the captured image.
	jsonFormat, JsonErr := json.MarshalIndent(image,"","     ")
	if JsonErr != nil {
		fmt.Println(JsonErr)
		return
	}

	// Print result in JSON format
	fmt.Println(string(jsonFormat))
}

```
