---
title: "Look up an SSH key"
description: "Look up information about an SSH key by its label.  Demonstrates
how to use the SDK's filter utility to apply an objectFilter to limit a result set"
date: "2016-09-19"
tags:
    - "Account"
    - "SshKey"
    - "filter"
---

```go
package main

import (
    "fmt"
    "log"

    "github.com/softlayer/softlayer-go/filter"
    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
)

// The key to look up
const label = "Test Public Key"

func main() {
    sess := session.New()
    service := services.GetAccountService(sess)

    keys, err := service.
        Filter(filter.Build(
            filter.Path("sshKeys.label").Eq(label))).
        Mask("id,label,key,fingerprint,notes").
        GetSshKeys()

    if err != nil {
        log.Fatal("Error retrieving SSH key: ", err)
    }

    if len(keys) == 0 {
        log.Fatal("No ssh key found labeled ", label)
    }

    if len(keys) > 1 {
        log.Fatal("More than one ssh key found labeled ", label)
    }

    key := keys[0]

    fmt.Printf("Public Key [%s] found:\n", label)

    fmt.Println("\tID:", *key.Id)
    fmt.Println("\tFingerprint:", *key.Fingerprint)
    fmt.Println("\tKey:", *key.Key)

    notes := ""
    if key.Notes != nil {
        notes = *key.Notes
    }

    fmt.Println("\tNotes:", notes)
}
```
