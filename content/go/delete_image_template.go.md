---
title: "delete_image_template.go"
description: "delete_image_template.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "image-templates"
---


```
/*
Delete an image template

The script makes a single call to the SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject
method to delete an image template. For more information see below.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key.
	username  := "set me"
	apikey    := "set me"

  	// The image id you wish to delete.
	imageId := 879951

	// Create session
  	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest_Block_Device_Template_Group service.
  	service := services.GetVirtualGuestBlockDeviceTemplateGroupService(sess)

	// Delete the image
  	result, err := service.Id(imageId).DeleteObject()
	if err != nil {
		fmt.Printf("\n Unable to delete image:\n - %s\n", err)
		return
	} 

	// Print result
  	fmt.Println(result)
}

```
