---
title: "Get disk usage metrics for a time range"
description: "Get the disk usage metrics for the most recent 24 hours. Also
demonstrates how to pass datetime values to the API"
date: "2016-09-19"
tags:
    - "Account"
    - "DateTime"
    - "getDiskUsageMetricDataByDate"
---

```go
package main

import (
    "fmt"
    "log"
    "time"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
    "github.com/softlayer/softlayer-go/sl"
)

func main() {
    // Create a session
    sess := session.New()

    // Account service has the method we need
    service := services.GetAccountService(sess)

    // Range: most recent 24 hours
    //
    // Time values are wrapped within an sl.Time type, to facilitate json marshaling
    tEnd := sl.Time(time.Now())
    tStart := sl.Time(tEnd.AddDate(0, 0, -1))

    data, err := service.GetDiskUsageMetricDataByDate(tStart, tEnd)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Number of elements returned: %d\n", len(data))

    for _, d := range data {
        fmt.Printf("Counter: %.f, Time: %s, Type: %s\n", *d.Counter, *d.DateTime, *d.Type)
    }
}
```
