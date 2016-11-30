---
title: "Handle API errors"
description: "This example shows how to handle specific errors (e.g., 404)
by type-asserting the returned error and inspecting its fields."
date: "2016-09-19"
tags:
    - "VirtualGuest"
    - "Errors"
---

```go
package main

import (
    "fmt"
    "log"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
    "github.com/softlayer/softlayer-go/sl"
)

var invalidId = 0

func main() {
    // Create a session
    sess := session.New()

    // Call DeleteObject on an invalid virtual guest
    _, err := services.GetVirtualGuestService(sess).
        Id(invalidId).
        DeleteObject()

    // Check the error.  In this instance, a 404 is handled by the application.  
  // Anything else is a no-go.
    if err != nil {
        // Try to type assert the error and look for http status code 404
        if apiErr, ok := err.(sl.Error); ok && apiErr.StatusCode == 404 {
            fmt.Println("Virtual Guest not found (already deleted?)")
        } else {
            log.Fatal("Unhandled error:", err)
        }
    }
}
```
