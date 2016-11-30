---
title: "Execute Remote Script"
description: "Example of running a remotely hosted script on a VM. Demonstrates
usage of Id() to specify the object to act on, as well as how to pass
parameters (script URL) to a service method"
date: "2016-09-19"
tags:
    - "VirtualGuest"
    - "objectid"
    - "parameters"
    - "executeRemoteScript"
---

```go
package main

import (
    "fmt"
    "log"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
)

var remoteScriptURL = "http://example.com/scripts/preparevm"

func main() {
    // Create a session
    sess := session.New()

    // Get the VirtualGuest service
    service := services.GetVirtualGuestService(sess)

    // Execute the script on VM with ID 12345678
    err := service.Id(12345678).ExecuteRemoteScript(&remoteScriptURL)

    if err != nil {
        log.Fatal(err)
    } else {
        fmt.Println("Remote script sent for execution")
    }
}
```
