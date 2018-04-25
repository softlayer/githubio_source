---
title: "get_object_account.go"
description: "get_object_account.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Account"
tags:
    - "examples"
---


```
/*
Get information about account

This is an example gets SoftLayer_Account information without using softlayer-go client.
On this case we will build a SoftLayerServiceRequest object which contains information about service
we want to send a request, this will be passed to UrlRequest() method to build the url of service
and finally we will make the request by using the method RestRequest().

Additionally we will show how to save the response data in an structure called 'Struct'.

See below for more details.

Important softlayer manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

import (
	"../slapi"
	"encoding/json"
	"fmt"
	"log"
)

// Structure used to save response data, on this case we will save the id, address1, and firstName.
type Account struct {
	Id int `json:"id"`
	Address1 string `json:"address1"`
	FirstName string `json:"firstName"`
}


func main() {

	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Build the SoftLayer request you want to send to the API by using REST
	slRequest := &slapi.SoftLayerServiceRequest{
		Endpoint: "https://api.softlayer.com/rest/v3",
		ServiceName: "SoftLayer_Account",
		Method: "getObject",
	}

	// Send API request
	response := slapi.RestRequest(slapi.UrlRequest(*slRequest), username, apikey, nil, "GET")
	defer response.Body.Close()

	// Following is used to save the response in the Account struct
	// Use json.Decode for reading streams of JSON data
	var record Account
	if err := json.NewDecoder(response.Body).Decode(&record); err != nil {
		log.Println(err)
	}

	// To verify that response was saved you can make a single print like below.
	fmt.Println("ID = ", record.Id)
	fmt.Println("FirstName = ", record.FirstName)
	fmt.Println("Address = ", record.Address1)
}

```
