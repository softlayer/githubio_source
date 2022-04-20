---
title: "Working with Subnets"
description: "A collection of CLI Examples on how to interact with Subnets."
date: "2022-04-19"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Account"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "subnets"
    - "vlans"
---

Read up on the [Golang Example Framework](/go/exampleFramework) for information on how to setup the CLI Framework to get this code to run easily.

## Canceling a Subnet

This script makes a paginated API call to [SoftLayer_Billing_Item::cancelItem()](/reference/services/SoftLayer_Billing_Item/cancelItem/).


```go
/*
Cancel a Subnet. Cancel network subnet using its billing Item.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// The id of Subnet you wish to get information about "Allowed Network Storages".
	subnetId := 259934

	// In order to cancel billing item of subnet we need to set following values
	cancelImmediately     := true
	cancelAssociatedItems := true
	reason                := "For testing purposes"
	customerNote          := "API test"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Subnet and SoftLayer_Billing_Item services
	subnetService := services.GetNetworkSubnetService(sess)
	billingService := services.GetBillingItemService(sess)

	// Get the billing item from Subnet
	billingItem, err := subnetService.Id(subnetId).GetBillingItem()
	if err != nil {
		fmt.Printf("\n Unable to get IP Addresses from Subnet:\n - %s\n", err)
		return
	}

	// Call th method SoftLayer_Billing_Item::cancelItem in order to cancel the Subnet service.
	// You can also use cancelService() instead of cancelItem() method to cancel immediately
	// without filling a reason or note.
	result, err := billingService.Id(*billingItem.Id).CancelItem(&cancelImmediately, &cancelAssociatedItems, &reason, &customerNote)
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	fmt.Println(result)
}

```

## Getting subnets of a VLAN

This script makes a paginated API call to [SoftLayer_Network_Vlan::getSubnets()](/reference/services/SoftLayer_Network_Vlan/getSubnets/).

```go
/*
Retrieve the subnets for a VLAN

Retrieve all the subnets for a determinate VLAN associated with a SoftLayer customer account
We do this with a call to the getSubnets() method in the SoftLayer_Network_Vlan API service.
See below for more details.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/

package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Vlan id you wish to get its subnets
	vlanId := 1054267

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Network_Vlan service
	service := services.GetNetworkVlanService(sess)

	// Object-Mask to get specific subnet's information
	mask := "id;networkIdentifier;cidr;subnetType;totalIpAddresses;usableIpAddressCount"

	// Call to getSubnets() in order to retrieve all vlan's subnets.
	subnets, err := service.Id(vlanId).Mask(mask).GetSubnets()
	if err != nil {
		fmt.Printf("\n Unable to get Vlan's subnets:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _,subnet := range subnets {
		jsonFormat, jsonErr := json.Marshal(subnet)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Println(string(jsonFormat))
	}
}

```

## Listing subnets

This script makes a paginated API call to [SoftLayer_Account::getSubnets()](/reference/services/SoftLayer_Account/getSubnets/).

```go
/*
List subnets. It retrieves all network subnets associated with an account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSubnets
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"encoding/json"
	"github.com/softlayer/softlayer-go/filter"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	/*
	Filter all subnets by subnetType, following are possible values:
	      PRIMARY_6, GLOBAL_IP, PRIMARY, STATIC_IP_ROUTED,
	      SECONDARY_ON_VLAN, ADDITIONAL_PRIMARY
	On this case we'll filter by 'PRIMARY' type.
	*/
	filter := filter.Path("subnets.subnetType").Eq("PRIMARY").Build()

	// Call method getSubnets() in order to get all subnets in the Account.
	subnets, err := service.Filter(filter).GetSubnets()
	if err != nil {
		fmt.Printf("\n Unable to get subnets:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	for _, subnet := range subnets {
		jsonFormat, jsonErr := json.Marshal(subnet)
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}

		fmt.Println(string(jsonFormat))
	}
}

```

## Creating subnets

These scripts make a paginated API call to [SoftLayer_Product_Order::verifyOrder()](/reference/services/SoftLayer_Product_Order/verifyOrder/).

### Ordering a new portable private subnet

```go
/*
Order a new portable private subnet.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
  	"encoding/json"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the quantity, location, and packageId for the subnet you wish to order.
	quantity  := 1
	packageId := 0
	location  := "DALLAS05"

	// The id of a Private Network Vlan. To get the list of vlans use the method
	// SoftLayer_Account::getPrivateNetworkVlans
	vlanId    := 865555

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(13981)},         // 4 Portable Private IP Addresses
	}

	// Build a skeleton Container_Product_Order_Network_Subnet object containing the order
	// you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_Subnet {
		Container_Product_Order : datatypes.Container_Product_Order {
			PackageId : sl.Int(packageId),
			Location  : sl.String(location),
			Quantity  : sl.Int(quantity),
			Prices    : prices,
		},
		EndPointVlanId : sl.Int(vlanId),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```

### Ordering a new portable public subnet

```go
/*
Order a new portable public subnet.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the quantity, location, and packageId for the subnet you wish to order.
	quantity  := 1
	packageId := 0
	location  := "SINGAPORE01"

	// The id of a Public Network Vlan. To get the list of vlans use the method
	// SoftLayer_Account::getPublicNetworkVlans
	vlanId    := 863477

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(13980)},          // 4 Portable Public IP Addresses
	}

	// Build a skeleton Container_Product_Order_Network_Subnet object containing the order
	// you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_Subnet {
		Container_Product_Order : datatypes.Container_Product_Order {
			PackageId : sl.Int(packageId),
			Location  : sl.String(location),
			Quantity  : sl.Int(quantity),
			Prices    : prices,
		},
		EndPointVlanId : sl.Int(vlanId),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```

### Ordering a new portable public subnet IPv6

```go
/*
Orders a new portable Public subnet IPv6

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
	"encoding/json"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the quantity, location, and packageId for the subnet you wish to order.
	quantity  := 1
	packageId := 0
	location  := "MEXICO"

	// The id of a Public Network Vlan. To get the list of vlans use the method
	// SoftLayer_Account::getPublicNetworkVlans
	vlanId    := 863477

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(1482)},          // 64 Block Portable Public IPv6 Addresses
	}

	// Build a skeleton Container_Product_Order_Network_Subnet object containing the order
	// you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_Subnet {
		Container_Product_Order : datatypes.Container_Product_Order {
			PackageId : sl.Int(packageId),
			Location  : sl.String(location),
			Quantity  : sl.Int(quantity),
			Prices    : prices,
		},
		EndPointVlanId : sl.Int(vlanId),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```

### Ordering a new static public subnet

```go
/*
Order a new static public subnet

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
  	"encoding/json"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the quantity, location, and packageId for the subnet you wish to order.
	quantity  := 1
	packageId := 0
	location  := "SINGAPORE01"

	// The id of a Public Ip Addresses. To get the list of ip address you can use the methods
	// SoftLayer_Account::getPublicIpAddresses, SoftLayer_Account::getIpAddresses
	ipAddressIp := 47665099

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(13983)},          // 1 Static Public IP Address
	}

	// Build a skeleton Container_Product_Order_Network_Subnet object containing the order
	// you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_Subnet {
		Container_Product_Order : datatypes.Container_Product_Order {
			PackageId : sl.Int(packageId),
			Location  : sl.String(location),
			Quantity  : sl.Int(quantity),
			Prices    : prices,
		},
		EndPointIpAddressId : sl.Int(ipAddressIp),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```

### Ordering a new static public subnet ipv6

```go
/*
Order a new static public subnet ipv6

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/sl"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Declare the quantity, location, and packageId for the subnet you wish to order.
	quantity  := 1
	packageId := 0
	location  := "SINGAPORE01"

	// The id of a Public Ip Addresses. To get the list of ip address you can use the methods
	// SoftLayer_Account::getPublicIpAddresses, SoftLayer_Account::getIpAddresses
	ipAddressIp := 47665101

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
	prices := []datatypes.Product_Item_Price{
		{ Id: sl.Int(1481)},          // 64 Block Static Public IPv6 Addresses
	}

	// Build a skeleton Container_Product_Order_Network_Subnet object containing the order
	// you wish to place.
	orderTemplate := datatypes.Container_Product_Order_Network_Subnet {
		Container_Product_Order : datatypes.Container_Product_Order {
			PackageId : sl.Int(packageId),
			Location  : sl.String(location),
			Quantity  : sl.Int(quantity),
			Prices    : prices,
		},
		EndPointIpAddressId : sl.Int(ipAddressIp),
	}

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "","     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
