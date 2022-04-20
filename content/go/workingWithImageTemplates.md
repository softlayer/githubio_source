---
title: "Working with Image Templates"
description: "A collection of CLI Examples on how to interact with Image Templates."
date: "2022-04-18"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Account"
tags:
    - "image-templates"
    - "package"
    - "network"
---

Read up on the [Golang Example Framework](/go/exampleFramework) for information on how to setup the CLI Framework to get this code to run easily.


## Creating an flex image from a Virtual Server

This script makes a paginated API call to [SoftLayer_Virtual_Guest::captureImage()](/reference/services/SoftLayer_Virtual_Guest/captureImage/).


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

## Deleting an image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::deleteObject()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject/).


```go
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

## Getting items from an image template

This script returns an array of SoftLayer_Product_Item objects which are part of a
SoftLayer_Virtual_Guest_Block_Device_Template_Group object).


```go
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

## Listing Image templates

This script makes a paginated API call to [SoftLayer_Account::getPrivateBlockDeviceTemplateGroups()](/reference/services/SoftLayer_Account/getPrivateBlockDeviceTemplateGroups/).


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

## Sharing image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::permitSharingAccess()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess/).


```go
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

## Unsharing image template

This script makes a paginated API call to [SoftLayer_Virtual_Guest_Block_Device_Template_Group::denySharingAccess()](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess/).


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
