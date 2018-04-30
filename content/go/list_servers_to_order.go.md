---
title: "list_servers_to_order.go"
description: "list_servers_to_order.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Product_Package_Server"
tags:
    - "baremetalservers"
---


```
/*
List all servers to order.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package_Server/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Package_Server/
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
  	"encoding/json"
	"github.com/softlayer/softlayer-go/filter"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

  	// Create SoftLayer API session
  	sess := session.New(username, apikey)

  	// Get SoftLayer_Product_Package_Server service
    	service := services.GetProductPackageServerService(sess)

	// In order to get all servers to order we will use the following filter
	filter := filter.Build(
		filter.Path("packageType").
		       In("BARE_METAL_CORE","BARE_METAL_CPU","BARE_METAL_CPU_FAST_PROVISION"),
	)

	/*
	You can also use the following structure to build the filter:

    	filter := `{"packageType": {
    			"operation": "in",
    			"options": [{
    				"name": "data",
    	           		"value": [ "BARE_METAL_CORE", "BARE_METAL_CPU",
    	           			   "BARE_METAL_CPU_FAST_PROVISION"
    	           		         ]
    	           		}]
    	           	}
    	           }`

	*/

  	// Call the method SoftLayer_Product_Package_Server::getAllObjects
	servers, err := service.Filter(filter).GetAllObjects()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,server := range servers {
		jsonFormat, jsonErr := json.Marshal(server)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```
