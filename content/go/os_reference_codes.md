---
title: "Get Operating System Reference Codes"
description: "Retrieve Virtual Guest creation options, and print a list of available OS reference codes"
date: "2016-09-19"
tags:
    - "VirtualGuest"
    - "getCreateObjectOptions"
    - "operatingSystemReferenceCode"
---

```go
package main

import (
    "fmt"
    "log"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
)

func main() {
    // Create a session
    sess := session.New()

    // Invoke the 'GetCreateObjectOptions' method from the Virtual_Guest service
    opts, err := services.GetVirtualGuestService(sess).GetCreateObjectOptions()
    if err != nil {
        log.Fatal(err)
    }

    // Available properties for inspection:
    //opts.BlockDevices
    //opts.Datacenters
    //opts.Memory
    //opts.NetworkComponents
    //opts.OperatingSystems
    //opts.Processors

    // Print all available OS reference codes:
    for _, os := range opts.OperatingSystems {
        fmt.Println(*os.Template.OperatingSystemReferenceCode)
    }
}
```
