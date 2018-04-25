---
title: "edit_gateway.go"
description: "edit_gateway.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
/*
Edit Network_Gateway object.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/editObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of gateway you wish to get its information 61522
	gatewayId := 244163

	// Build Network_Gateway skeleton in order to pass it to editObject() method.
	// Currently, the only value that can be edited is the name.
	templateObject := datatypes.Network_Gateway{
		Name: sl.String("New gateway's name"),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Gateway service
	service := services.GetNetworkGatewayService(sess)

	// Call to editObject() method in order to change the Gateway's name
	result, err := service.Id(gatewayId).EditObject(&templateObject)
	if err != nil {
		fmt.Printf("\n Unable to edit gateway object:\n - %s\n", err)
		return
	}

	fmt.Println(result)
}

```
