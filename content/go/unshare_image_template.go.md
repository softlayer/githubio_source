---
title: "unshare_image_template.go"
description: "unshare_image_template.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "image-templates"
---


```go
/*
Un-share an image template

The script un-shares an image template it makes a call to  SoftLayer_Virtual_Guest_Block_Device_Template_Group::denySharingAccess
method for more information please see below:

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess
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

  	// The image id you wish to remove sharing access
	imageId := 879951

	// The account you wish to remove sharing access
	accountToShare := 207819

	// Create session
  	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest_Block_Device_Template_Group service.
  	service := services.GetVirtualGuestBlockDeviceTemplateGroupService(sess)

	// Un-share the image.
  	result, err := service.Id(imageId).DenySharingAccess(&accountToShare)
	if err != nil {
		fmt.Printf("\n Unable to remove sharing access:\n - %s\n", err)
		return
	} 

	// Print result
  	fmt.Println(result)
}

```
