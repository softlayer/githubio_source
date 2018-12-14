---
title: "Working with placement groups"
description: "A few examples on interacting with placement group"
date: "2018-12-14"
classes: 
    - "SoftLayer_Virtual_PlacementGroup"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Account"
tags:
    - "order"
    - "Account"
    - "Virtual"
---

Create Placement Group

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {

	username := "set me"
	apikey := "set me"
	
	sess := session.New(username, apikey)
	service := services.GetVirtualPlacementGroupService(sess)

	templateObject := datatypes.Virtual_PlacementGroup{

		Name:            sl.String("test"),
		BackendRouterId: sl.Int(12345),
		RuleId:          sl.Int(1),
	}
	receipt, err := service.CreateObject(&templateObject)
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}

	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```

Delete Placement Group

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {

	username := "set me"
	apikey := "set me"
	
	placementId := 12345

	sess := session.New(username, apikey)

	service := services.GetVirtualPlacementGroupService(sess)

	receipt, err := service.Id(placementId).DeleteObject()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}

	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}
```

Get Guests from a Placement Group

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {

	username := "set me"
	apikey := "set me"

	placementId := 12345

	sess := session.New(username, apikey)

	service := services.GetVirtualPlacementGroupService(sess)

	receipt, err := service.Id(placementId).GetGuests()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}

	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}
```

Get Placement Groups of the Account

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {

	username := "set me"
	apikey := "set me"
	
	sess := session.New(username, apikey)
	accountService := services.GetAccountService(sess)

	receipt, err := accountService.GetPlacementGroups()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}

	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}
```

Order a Virtual Guest into a specific Placement Group

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {

	username := "set me"
	apikey := "set me"

	sess := session.New(username, apikey)

	quantity := 1
	location := "448994"
	packageId := 835
	presetId := 215
	hostname := "softlayer"
	domain := "example.com"
	placementId := 12345

	virtualGuests := []datatypes.Virtual_Guest{
		{
			Hostname:         sl.String(hostname),
			Domain:           sl.String(domain),
			PlacementGroupId: sl.Int(placementId),
		},
	}

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{Id: sl.Int(203967)},
		{Id: sl.Int(204135)},
		{Id: sl.Int(45466)},
		{Id: sl.Int(2202)},
		{Id: sl.Int(204853)},
		{Id: sl.Int(1800)},
		{Id: sl.Int(273)},
		{Id: sl.Int(17129)},
		{Id: sl.Int(28)},
		{Id: sl.Int(55)},
		{Id: sl.Int(58)},
		{Id: sl.Int(420)},
		{Id: sl.Int(418)},
		{Id: sl.Int(21)},
		{Id: sl.Int(57)},
		{Id: sl.Int(905)},
	}

	orderTemplate := datatypes.Container_Product_Order{
		Quantity:      sl.Int(quantity),
		Location:      sl.String(location),
		PackageId:     sl.Int(packageId),
		PresetId:      sl.Int(presetId),
		Prices:        prices,
		VirtualGuests: virtualGuests,
	}

	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```

Get the Placement Group from a Virtual Guest

```go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {

	username := "set me"
	apikey := "set me"
	
	guestId := 12345678
	sess := session.New(username, apikey)

	service := services.GetVirtualGuestService(sess)

	receipt, err := service.Id(guestId).GetPlacementGroup()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}

	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
