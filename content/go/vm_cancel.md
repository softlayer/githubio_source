---
title: "Cancel a virtual guest"
description: "Example of how to cancel a virtual guest."
date: "2016-09-19"
tags:
    - "VirtualGuest"
---

```go
package main

import (
	"fmt"
	"log"

	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

var guestId = 24438563

func main() {
	// Create a session
	sess := session.New()

	// Get the virtual guest service
	service := services.GetVirtualGuestService(sess)

	// Set the object ID and delete the guest
	success, err := service.Id(guestId).DeleteObject()

	if err != nil {
		log.Fatal(err)
	} else if success == false {
		log.Fatal("Error deleting virtual guest")
	} else {
		fmt.Println("Virtual Guest deleted successfully")
	}
}
```
