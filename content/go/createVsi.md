---
title: "Creating a Virtual Guest"
description: "Creates a new virtual server (VSI) and demonstrates the many options that can be used to customize the creation. ."
date: "2016-11-07"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "virtualGuests"
    - "CreateObject"
---

```go

package main

import (
    "fmt"
    "github.com/softlayer/softlayer-go/datatypes"
    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
    "github.com/softlayer/softlayer-go/sl"
)

func main() {
    sess := session.New()
    doCreateVMTest(sess)
}


func doCreateVMTest(sess *session.Session) {
    service := services.GetVirtualGuestService(sess)

    // Create a Virtual_Guest instance as a template
    vGuestTemplate := datatypes.Virtual_Guest{}

    //Set Creation values - use helpers from the sl package to set pointer values
    vGuestTemplate.Hostname = sl.String("sample")
    vGuestTemplate.Domain = sl.String("example.com")
    vGuestTemplate.MaxMemory = sl.Int(4096)
    vGuestTemplate.StartCpus = sl.Int(1)
    vGuestTemplate.Datacenter = &datatypes.Location{Name: sl.String("wdc01")}
    vGuestTemplate.OperatingSystemReferenceCode = sl.String("UBUNTU_LATEST")
    vGuestTemplate.LocalDiskFlag = sl.Bool(true)

    vGuest, err := service.Mask("id;domain").CreateObject(&vGuestTemplate)
    if err != nil {
        fmt.Printf("%s\n", err)
        return
    } else {
        fmt.Printf("\nNew Virtual Guest created with ID %d\n", *vGuest.Id)
        fmt.Printf("Domain: %s\n", *vGuest.Domain)
    }
}

```
