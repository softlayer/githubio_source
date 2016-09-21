---
title: "List SSH Keys"
description: "Get a list of SSH Key IDs and labels under your SoftLayer account"
date: "2016-09-19"
tags:
    - "SshKey"
    - "getSshKeys"
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
	// Create a session, using credentials from the environment or a .softlayer file
	sess := session.New()

	// Get an instance of the Account service
	service := services.GetAccountService(sess)

	// invoke the GetSshKeys API method
	keys, err := service.Mask("id,label").GetSshKeys()
	if err != nil {
		log.Fatal(err)
	} else {
		for _, key := range keys {
			fmt.Printf("\t[%d] %s\n", *key.Id, *key.Label)
		}
	}
}
```
