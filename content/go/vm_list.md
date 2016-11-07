---
title: "List Account VMs"
description: "Basic example showing how to get a list of Virtual Guests under an account"
date: "2016-09-19"
tags:
    - "VirtualGuest"
    - "getVirtualGuests"
---

```go
package main

import (
    "fmt"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
)

func main() {
  // Create a session, using credentials from the environment or a .softlayer file
    sess := session.New()

  // Get an instance of the Account service
    service := services.GetAccountService(sess)

  // invoke the GetVirtualGuests API method
    vms, err := service.Mask("id;hostname;domain").GetVirtualGuests()
    if err != nil {
        fmt.Printf("Error retrieving Virtual Guests from Account: %s\n", err)
    } else {
        fmt.Println("VMs under Account:")

    for _, vm := range vms {
      fmt.Printf("\t[%d]%s.%s\n", *vm.Id, *vm.Hostname, *vm.Domain)
    }
    }
}
```
