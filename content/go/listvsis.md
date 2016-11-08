---
title: "Listing Virtual Guests"
description: "A Go example to list Virtual Guests on an account."
date: "2016-11-07"
classes: ["SoftLayer_Account"]
tags:
    - "virtualGuests"
---

```go
package main

import (
	"fmt"

	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
  "github.com/softlayer/softlayer-go/sl"
)

func main() {

          sess := session.New()
          doListAccountVMsTest(sess)
}

func doListAccountVMsTest(sess *session.Session) {
	// Get the Account service
	service := services.GetAccountService(sess)

	// List VMs
	vms, err := service.Mask("id;hostname;domain").Limit(10).GetVirtualGuests()
	if err != nil {
		fmt.Printf("Error retrieving Virtual Guests from Account: %s\n", err)
		return
	} else {
		fmt.Println("VMs under Account:")
	}

	for _, vm := range vms {
		fmt.Printf("\t[%d]%s.%s\n", *vm.Id, *vm.Hostname, *vm.Domain)
	}
}

func handleError(err error) {
	apiErr := err.(sl.Error)
	fmt.Printf(
		"Exception: %s\nMessage: %s\nHTTP Status Code: %d\n",
		apiErr.Exception,
		apiErr.Message,
		apiErr.StatusCode)
}
```
