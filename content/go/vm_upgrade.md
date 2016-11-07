---
title: "Upgrade a virtual guest"
description: "This example demonstrates the use of helper functions that
simplify the process of placing a virtual guest upgrade order"
date: "2016-09-19"
tags:
    - "VirtualGuest"
    - "UpgradeVirtualGuest"
---

```go
package main

import (
	"fmt"
	"log"

	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/helpers/product"
	"github.com/softlayer/softlayer-go/helpers/virtual"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

const guestID = 123456

func main() {
	sess := session.New()

	// Create a minimal Virtual_Guest object to pass to the upgrade helper
	guestToUpgrade := datatypes.Virtual_Guest{
		Id: sl.Int(guestID),
	}

	// Upgrade to 4 Core, 8 GB
	upgradeOptions := map[string]float64{
		product.CPUCategoryCode:    float64(4),
		product.MemoryCategoryCode: float64(8),
	}

	receipt, err := virtual.UpgradeVirtualGuest(sess, &guestToUpgrade, upgradeOptions)
	if err != nil {
		log.Fatal("Couldn't upgrade virtual guest:", err)
	}

	fmt.Printf("Virtual Guest upgrade submitted.  Order ID: %s\n", *receipt.OrderId)
}
```
