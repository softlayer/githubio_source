---
title: "list_images_templates.go"
description: "list_images_templates.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
tags:
    - "image-templates"
---


```go
/*
Get private image templates

The script calls the SoftLayer_Account::getPrivateBlockDeviceTemplateGroups method to list the
private templates in the account and uses an object mask to display more related information of
the images templates.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups
http://sldn.softlayer.com/reference/dataypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key.
	username  := "set me"
	apikey    := "set me"

	// Create session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service.
	service := services.GetAccountService(sess)

	// Declare mask that will be used to get specific data
	mask:="id,name,parentId,userRecordId,summary,note,status[name]," +
		"storageRepository[datacenter];imageTypeKeyName"

	// Retrieve image templates from account.
	images, err := service.Mask(mask).GetPrivateBlockDeviceTemplateGroups()
	if err != nil {
		fmt.Printf("\n Unable to retrieve image templates:\n - %s\n", err)
		return
	}

	// Following creates a JSON object which is based on data of the captured image.
	for _, image := range images {
		jsonFormat, JsonErr := json.Marshal(image)
		if JsonErr != nil {
			fmt.Println(JsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}

}

```
