---
title: "list_permission_roles.go"
description: "list_permission_roles.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_User_Permission_Role"
tags:
    - "brands"
---


```go
/*
List roles.

The script retrieves all the roles in a brand account.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getPermissionRoles
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Permission_Role

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Retrieve permission roles
	permissions, err := service.GetPermissionRoles()
	if err != nil {
		fmt.Printf("\n Unable to retrieve permission roles - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, role := range permissions {
		jsonFormat, jsonErr := json.Marshal(role)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```
