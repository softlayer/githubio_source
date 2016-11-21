---
title: "Provision a virtual guest"
description: "Example of provisioning a virtual guest from a template object."
date: "2016-09-19"
tags:
    - "VirtualGuest"
---

```go
package main

import (
    "fmt"
    "log"

    "github.com/softlayer/softlayer-go/datatypes"
    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
    "github.com/softlayer/softlayer-go/sl"
)

// A virtual guest template
//
// (use convenience functions to get pointers from literals, as needed)
var vGuestTemplate = datatypes.Virtual_Guest{
    Hostname:                     sl.String("sample"),
    Domain:                       sl.String("example.com"),
    MaxMemory:                    sl.Int(4096),
    StartCpus:                    sl.Int(1),
    Datacenter:                   &datatypes.Location{Name: sl.String("wdc01")},
    OperatingSystemReferenceCode: sl.String("UBUNTU_LATEST"),
    LocalDiskFlag:                sl.Bool(true),
}

func main() {
    // Create a session
    sess := session.New()

    service := services.GetVirtualGuestService(sess)

    // Create the virtual guest from the template
    //
    // We also specify an (optional) object mask, to read back some values
    vGuest, err := service.Mask("id,hostname,domain").CreateObject(&vGuestTemplate)
    if err != nil {
        log.Fatal(err)
    } else {
        fmt.Printf(
            "\nNew Virtual Guest with ID %d being provisioned\n", *vGuest.Id)
    }
}
```
