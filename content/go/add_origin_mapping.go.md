---
title: "add_origin_mapping.go"
description: "add_origin_mapping.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping"
tags:
    - "cdn"
---


```
/*
Create an origin mappings in a CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullMapping
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of CDN Account you wish to add an origin pull mapping
	cdnId := 8166

	// Declare the mediaType, originURL and cname
	mediaType := "HTTP"
	originUrl := "http://www.example.com"
	cname     := "cdn.softlayer-example.com"

	// Build the SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping template object
	// that will be used to create the origin pull mapping.
	templateObject := datatypes.Container_Network_ContentDelivery_OriginPull_Mapping{
		MediaType: sl.String(mediaType),
		OriginUrl: sl.String(originUrl),
		Cname: sl.String(cname),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_ContentDelivery_Account service
	service := services.GetNetworkContentDeliveryAccountService(sess)

	// Call the createOriginPullMapping() method to create a new mapping
	result, err := service.Id(cdnId).CreateOriginPullMapping(&templateObject)
	if err != nil {
		fmt.Printf("\n Unable to create an origin pull mapping for CDN:\n - %s\n", err)
		return
	}

	fmt.Println(result)
}

```
