---
title: "cancel_portable_storage.go"
description: "cancel_portable_storage.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Storage_Repository"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Virtual_Disk_Image"
tags:
    - "portablestorage"
---


```
/*
Cancel a Portable Storage

This example shows how to cancel a Portable Storage object. Take account that Portal Storage objects
must be unattached in order to be canceled.
See below for more details.

Important manual pages:

http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Disk_Image/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Disk_Image
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Storage_Repository
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id  of Portable Storage volume you wish to cancel.
	storageId := 25552937

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Virtual_Disk_Image and SoftLayer_Billing_Item services
	storageService  := services.GetVirtualDiskImageService(sess)
	billingService  := services.GetBillingItemService(sess)

	// Declare mask used to get the id of billing item and associated guests
	mask := "id;billingItem[id];storageRepository[guests]"

	// Call to getObject() method in order to get storage data according to mask
	storage, err := storageService.Id(storageId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get the Portable Storage\n - %s\n", err)
		return
	}

	// Before to cancel storage service, we'll verify that it isn't attached to another device.
	if storage.StorageRepository != nil {
		if len(storage.StorageRepository.Guests) != 0 {
			fmt.Printf("\n The portable storage volume '%d' can not be cancelled" +
				" while attached to another device\n", storageId)
		} else {
			// Call to Billing_Item::cancelService method to cancel the unattached
			// portable storage volume.
			result, err := billingService.Id(*storage.BillingItem.Id).CancelService()
			if err != nil {
				fmt.Printf("\n Unable to cancel Portable Storage volume\n - %s\n", err)
				return
			}

			// Print final result
			if result {
				fmt.Printf("\n Portable Storage '%d' was successfuly cancelled\n", storageId)
			} else {
				fmt.Printf("\n Portable Storage '%d' could not be cancelled\n", storageId)
			}
		}
	}
}

```
