---
title: "Working with placement groups"
description: "A few examples on interacting with placement group"
date: "2019-01-11"
classes: 
    - "SoftLayer_Virtual_PlacementGroup"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Account"
tags:
    - "order"
    - "account"
    - "virtual"
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

	// Create a session
	sess := session.New()
	
	// Get SoftLayer_Virtual_PlacementGroup service.
	service := services.GetVirtualPlacementGroupService(sess)

	// A Virtual_PlacementGroup template
	templateObject := datatypes.Virtual_PlacementGroup{

		Name:            sl.String("test"),
		BackendRouterId: sl.Int(12345),
		RuleId:          sl.Int(1),
	}
	
	// Get SoftLayer_Virtual_PlacementGroup service.
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


	//Placement group's associated unique ID.
	placementId := 12345
	
    // Create a session
	sess := session.New()
	
    // Get SoftLayer_Virtual_PlacementGroup service.
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

    //Placement group's associated unique ID.
	placementId := 12345
	
    // Create a session
	sess := session.New()

    // Get SoftLayer_Virtual_PlacementGroup service.
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

	// Create a session
	sess := session.New()
	
	// Get SoftLayer_Account service.
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

    // Create a session
    	sess := session.New()
    
    	quantity := 1
    	location := "TORONTO"
    	packageId := 835
    	presetId := 215
    	hostname := "test"
    	domain := "example.com"
    	placementId := 12345
    
    	virtualGuests := []datatypes.Virtual_Guest{
    		{
    			Hostname:         sl.String(hostname),
    			Domain:           sl.String(domain),
    			PlacementGroupId: sl.Int(placementId),
    		},
    	}
    
    	/*
    	List of minimal required items for ordering VSI:
    		 -Computing Instance
    		 -RAM
    		 -First Disk
    		 -Remote Management
    		 -Uplink Port Speeds
    		 -Public Bandwidth
    		 -Primary IP Addresses
    		 -Operating System
    		 -Monitoring
    		 -Notification
    		 -Response
    		 -VPN Management - Private Network
    		 -Vulnerability Assessments & Management
    	Computing Instance, RAM, First Hard Drive are covered by the preset.
    	*/
    
    	orderItems := [] string{
    		"REBOOT_REMOTE_CONSOLE",
    		"100_MBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS",
    		"BANDWIDTH_20000_GB",
    		"1_IP_ADDRESS",
    		"OS_CENTOS_7_X_MINIMAL_64_BIT",
    		"MONITORING_HOST_PING_AND_TCP_SERVICE",
    		"NOTIFICATION_EMAIL_AND_TICKET",
    		"AUTOMATED_REBOOT_FROM_MONITORING",
    		"UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT",
    	}
    	// Build a skeleton SoftLayer_Product_Item_Price objects.
    	prices := getItemPriceList(sess, packageId, orderItems)
    
    	// Build a container_Product_Order object.
    	orderTemplate := datatypes.Container_Product_Order{
    		Quantity:      sl.Int(quantity),
    		Location:      sl.String(location),
    		PackageId:     sl.Int(packageId),
    		PresetId:      sl.Int(presetId),
    		Prices:        prices,
    		VirtualGuests: virtualGuests,
    	}
    	// Get SoftLayer_Product_Order service.
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
    
    /**
    Converts a list of item keyNames to a list of item prices
    given package associated with the prices and a list itemsKeyNames.
     */
    func getItemPriceList(sess *session.Session, packageId int, itemKeyNames [] string) (resp []datatypes.Product_Item_Price) {
    
    	items := listPackageItems(sess, packageId)
    	var prices []datatypes.Product_Item_Price
    	for _, itemKeyName := range itemKeyNames {
    		for _, item := range items {
    			if (*item.KeyName) == itemKeyName {
    				for _, itemPrice := range item.Prices {
    					if itemPrice.LocationGroupId == nil {
    						prices = append(prices, itemPrice)
    						break
    					}
    				}
    
    			}
    		}
    	}
    	return prices
    }
    
    //List the items for the given package.
    func listPackageItems(sess *session.Session, packageId int) (resp []datatypes.Product_Item) {
    	var mask = "id, itemCategory, keyName, prices[id,categories]"
    	var service = services.GetProductPackageService(sess)
    	receipt, err := service.Id(packageId).Mask(mask).GetItems()
    	if err != nil {
    		fmt.Printf("\n Unable to get Items:\n - %s\n", err)
    		return
    	}
    
    	return receipt
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

    // Unique ID for a computing instance.
	guestId := 12345678
	
	// Create a session		
	sess := session.New()

    // Get SoftLayer_Virtual_Guest service.
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
