---
title: "delete_origin_mapping.go"
description: "delete_origin_mapping.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping"
tags:
    - "cdn"
---


```go
/*
Delete an origin mappings in a CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/deleteOriginPullRule
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of CDN Account you wish to delete an origin mapping
	cdnId := 8166

	// The id of origin pull mapping you wish to delete
	originId := "op1689589"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_ContentDelivery_Account service
	service := services.GetNetworkContentDeliveryAccountService(sess)

	// Call the deleteOriginPullRule() method to delete the origin mapping
	result, err := service.Id(cdnId).DeleteOriginPullRule(sl.String(originId))
	if err != nil {
		fmt.Printf("\n Unable to delete origin pull mapping from CDN:\n - %s\n", err)
		return
	}

	fmt.Println(result)
}

```
