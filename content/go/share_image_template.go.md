---
title: "share_image_template.go"
description: "share_image_template.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "image-templates"
---


```
/*
Share image template.

The script shares an image template to another account, it makes a single call to
SoftLayer_Virtual_Guest_Block_Device_Template_Group::permitSharingAccess method.
For more information please see below.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess
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

  	// The image id you wish to share
	imageId := 879951

	// The account you wish to share the image template
	accountToShare := 207819

	// Create session
  	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Guest_Block_Device_Template_Group service.
  	service := services.GetVirtualGuestBlockDeviceTemplateGroupService(sess)
	// Share the image to specified account.
  	result, err := service.Id(imageId).PermitSharingAccess(&accountToShare)
	if err != nil {
		fmt.Printf("\n Unable to share the image:\n - %s\n", err)
		return
	} 

	// Print result
  	fmt.Println(result)
}

```
