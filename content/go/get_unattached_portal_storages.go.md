---
title: "get_unattached_portal_storages.go"
description: "get_unattached_portal_storages.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_Disk_Image"
tags:
    - "portablestorage"
---


```
/*
Get unattached portal storages.

The script gets all unattached portal storages in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPortableStorageVolumes
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Disk_Image

@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

import (
	"fmt"
  	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
  	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

  	// Create a session
  	sess := session.New(username, apikey)

  	// Get SoftLayer_Account service
  	service := services.GetAccountService(sess)

	// Use masks in order to get Guests of StorageRepositories
  	mask := "storageRepository[guests]"

	// All unattached storage objects will be saved here.
	unattachedStorages := []datatypes.Virtual_Disk_Image {}

  	// Get all portable storage volumes
	portableStorages, err := service.Mask(mask).GetPortableStorageVolumes()
	if err != nil {
		fmt.Printf("\n Unable to retrieve Portable Storages:\n - %s\n", err)
		return
	}

	// Search and save all unattached storages
  	for _,storage := range portableStorages {
		if storage.StorageRepository != nil {
      			if len(storage.StorageRepository.Guests) == 0 {
				unattachedStorages = append(unattachedStorages, storage)
      			}
    		}
  	}

	// Following helps to print the result in json format.
	for _,storage := range unattachedStorages {
		jsonFormat, jsonErr := json.Marshal(storage)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```
