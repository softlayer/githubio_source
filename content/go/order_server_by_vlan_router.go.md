---
title: "Order a Virtual and Bare Metal Server by frondend/backend vlan or router"
description: "Examples to order a Virtual and Bare Metal Server by frondend/backend vlan or router."
date: "2021-06-30"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Account"
tags:
    - "order"
    - "vlan"
    - "pricing"
    - "create"
    - "filter"
    - "hardware"
    - "package"
    - "router"
           
---

### Order a Bare Metal by frondend/backend vlan or router.

1. Find the package that you want to order. listServerPackages() will filter out all that are not bare metal 
    servers.

2. Use getServerPrices() to find the item keyNames you want to include in your order. These price IDs can be 
    included prices array directly, but I’ve included gatherPriceIds() to match up KeyNames to build a list of price 
    ids. getServerPrices() will also show the locations available for ordering.

3. listAvailableVlans() if you want to place the server on a specific VLAN.

4. listAvailableRouters() if you want to place the server on a specific router.

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

// Create the session and services
var sess = session.New()
var packageService = services.GetProductPackageService(sess)
var orderService = services.GetProductOrderService(sess)
var accountServer = services.GetAccountService(sess)

// Parameters will help us to reduce the number of argument in a function.
type Parameters struct {
	hostname             string
	domain               string
	packageId            int
	hourly               bool
	location             string
	items                []string
	backend              int
	frontend             int
	networkComponentType string
}

func main() {
	/**
	Step 1, Find the processor type you want
	553  Dual E5-2600 v4 Series (12 Drives)  DUAL_E52600_V4_12_DRIVES  BARE_METAL_CPU

	Remove the comment '//' below to get the 'listServerPackages()' information.
	*/

	ListServerPackage()
	//packageId := 553

	/**
	Step 2, Collect all the pieces you want to order
	getServerPrices will list out all the keyNames and cost of components
	that can be ordered on a certain package. Will also list the DCs that this
	server is available in.

	Remove the comment '//' below to 'getServerPrices()' information.
	*/

	//GetServerPrices(packageId)
	//locationId := 138124

	/**
	Step 3, Will list all available public and private vlans.

	Remove the comment '//' below to 'listAvailableVlans()' information.
	*/

	//ListAvailableVlans(locationId)
	//pubVlanId := 1111
	//privVlanId := 2222

	/**
	Step 4, Will list all available routers.

	Remove the comment '//' below to 'listAvailableRouters()' information.
	*/

	//ListAvailableRouters(locationId)
	//pubRouterId := 3333
	//privRouterId := 4444

	/**
	Step 5, To order a bare metal server by backend/frontend vlan.

	Remove the comment '//' below to order a bare metal server.
	*/

	//locationKeyName := "DALLAS05"

	//OrderHardwareServer(packageId, locationKeyName, pubVlanId, privVlanId, "vlan")

	/**
	Step 6, To order a bare metal server by backend/frontend router.

	Remove the comment '//' below to order a bare metal server.
	*/

	//OrderHardwareServer(packageId, locationKeyName, pubRouterId, privRouterId, "router")
}

func OrderHardwareServer(packageId int, locationKeyName string, frontend int, backend int, networkComponentType string) {
	// KeyNames of the items
	items := []string{
		"AUTOMATED_NOTIFICATION",
		"MONITORING_HOST_PING",
		"NOTIFICATION_EMAIL_AND_TICKET",
		"REBOOT_KVM_OVER_IP",
		"NESSUS_VULNERABILITY_ASSESSMENT_REPORTING",
		"UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT",

		"BANDWIDTH_500_GB",
		"1_IP_ADDRESS",
		"100_MBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS",

		"DISK_CONTROLLER_NONRAID",
		"HARD_DRIVE_1_00_TB_SATA_2",
		"RAM_64_GB_DDR4_2133_ECC_NON_REG",
		"OS_WINDOWS_2016_FULL_STD_64_BIT",
		"INTEL_INTEL_XEON_E52620_V4_2_10",
	}

	parameters := Parameters{
		hostname:             "myhostname",
		domain:               "domain.com",
		backend:              backend,
		frontend:             frontend,
		networkComponentType: networkComponentType,
		items:                items,
		location:             locationKeyName,
		packageId:            packageId,
	}

	prices := GetPrices(packageId, items)

	// Build the Hardware Server array object.
	hardware := BuildArrayHardwareServer(parameters)

	// Build the Container_Product_Order with the basic required data.
	containerOrder := datatypes.Container_Product_Order{
		PackageId: sl.Int(parameters.packageId),
		Location:  sl.String(parameters.location),
		Hardware:  hardware,
		Prices:    prices,
	}

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := orderService.VerifyOrder(&containerOrder)
	if err != nil {
		fmt.Printf("Unable to verify/place the order: %s", err)
	}

	// pretty print
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "   ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

func GetServerPrices(packageID int) {
	mask := "mask[regions,items[prices],activeServerItems[prices]]"
	result, err := packageService.Mask(mask).Id(packageID).GetObject()
	if err != nil {
		fmt.Printf("Unable to retrieve items: %s\n", err)
		os.Exit(1)
	}

	fmt.Println("---------------- Locations -------------------")
	fmt.Printf("| %10s | %20s |\n", "Location Id", "Location Name")
	for _, location := range result.Regions {
		fmt.Printf("| %10d ", *location.Location.Location.Id)
		fmt.Printf("| %20s |\n", *location.Description)
	}

	cores := "-"
    recurringFee := 0.0
	fmt.Println("----------------------------------------- Item Prices ------------------------------------------")
	fmt.Printf("| %10s | %50s | %10s | %10s | %40s |\n", "Price Id", "Description", "Cores", "Monthly Fee", "KeyName")
	for _, item := range result.Items {
		for _, price := range item.Prices {
			if price.LocationGroupId == nil {
                if price.RecurringFee != nil {
					recurringFee = float64(*price.RecurringFee)
				}
				if price.CapacityRestrictionType != nil {
					cores = fmt.Sprintf("%s - %s", *price.CapacityRestrictionMinimum, *price.CapacityRestrictionMaximum)

					fmt.Printf("| %10d ", *price.Id)
					fmt.Printf("| %50s ", *item.Description)
					fmt.Printf("| %10s ", cores)
					fmt.Printf("| %10f ", *price.RecurringFee)
					fmt.Printf("| %40s |\n", *item.KeyName)
				} else {
					fmt.Printf("| %10d ", *price.Id)
					fmt.Printf("| %50s ", *item.Description)
					fmt.Printf("| %10s ", cores)
					fmt.Printf("| %10f ", *price.RecurringFee)
					fmt.Printf("| %40s |\n", *item.KeyName)
				}
			}
		}
	}
}

func ListServerPackage() {
	objFilter := filter.Path("type.keyName").Eq("BARE_METAL_CPU").Build()
	packages, err := packageService.Mask("mask[type]").Filter(objFilter).GetAllObjects()
	if err != nil {
		fmt.Printf("Package %s doesn't exists\n", "BARE_METAL_CPU")
		os.Exit(1)
	}
	fmt.Printf("| %10s | %45s | %45s | %20s |\n", "Id", "Name", "KeyName", "Type")
	for _, item := range packages {
		fmt.Printf("| %10d ", *item.Id)
		fmt.Printf("| %45s ", *item.Name)
		fmt.Printf("| %45s ", *item.KeyName)
		fmt.Printf("| %20s |\n", *item.Type.KeyName)
	}
}

// GetPrices returns the list of prices.
func GetPrices(packageID int, itemKeyNames []string) []datatypes.Product_Item_Price {
	objMask := "mask[id,itemCategory,keyName,prices[categories]]"

	items, err := packageService.Mask(objMask).Id(packageID).GetItems()
	if err != nil {
		fmt.Printf("Unable to retrieve items: %s\n", err)
		os.Exit(1)
	}

	prices := make([]datatypes.Product_Item_Price, len(itemKeyNames))

	for idx, itemKeyName := range itemKeyNames {
		prices[idx].Id, err = GetPriceIDIfMatch(itemKeyName, items)
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
	}

	return prices
}

// GetPriceIDIfMatch returns a priceID or error if keyName doesnt exists.
func GetPriceIDIfMatch(keyName string, items []datatypes.Product_Item) (priceID *int, err error) {
	var matchingItem datatypes.Product_Item
	// find the item keyname
	for _, item := range items {
		if keyName == *item.KeyName {
			matchingItem = item
			break
		}
	}
	// returns error if keyName doesn't exists in the items list
	if matchingItem.KeyName == nil {
		return nil, fmt.Errorf("The item %s doesn't exists in the package", keyName)
	}
	// find the standard priceID
	for _, price := range matchingItem.Prices {
		if price.LocationGroupId == nil {
			priceID = price.Id
			break
		}
	}

	return
}

// BuildArrayHardwareServer builds the esqueleton of Hardware Server array.
func BuildArrayHardwareServer(args Parameters) []datatypes.Hardware {
	hardware := []datatypes.Hardware{
		{
			Hostname: sl.String(args.hostname),
			Domain:   sl.String(args.domain),
		},
	}

	if args.networkComponentType == "vlan" {
		if args.backend > 0 {
			hardware[0].PrimaryBackendNetworkComponent = &datatypes.Network_Component{
				NetworkVlan: &datatypes.Network_Vlan{
					Id: sl.Int(args.backend),
				},
			}
		}

		if args.frontend > 0 {
			hardware[0].PrimaryNetworkComponent = &datatypes.Network_Component{
				NetworkVlan: &datatypes.Network_Vlan{
					Id: sl.Int(args.frontend),
				},
			}
		}
	} else {
		if args.backend > 0 {
			hardware[0].PrimaryBackendNetworkComponent = &datatypes.Network_Component{
				Router: &datatypes.Hardware{
					Id: sl.Int(args.backend),
				},
			}
		}

		if args.frontend > 0 {
			hardware[0].PrimaryNetworkComponent = &datatypes.Network_Component{
				Router: &datatypes.Hardware{
					Id: sl.Int(args.frontend),
				},
			}
		}
	}
	return hardware
}

func ListAvailableVlans(locationId int) {
	objMask := "mask[billingItem[location]]"
	objFilter := filter.Path("publicNetworkVlans.billingItem.location.id").Eq(locationId).Build()

	publicVlans, err := accountServer.Mask(objMask).Filter(objFilter).GetPublicNetworkVlans()
	if err != nil {
		fmt.Printf("Unable to retrieve the publicVlans: %s\n", err)
		os.Exit(1)
	}

	fmt.Println("---------------------------------- PUBLIC VLANS ---------------------------------------")

	fmt.Printf("| %10s | %20s |%20s |%20s | \n", "Id", "Name", "VlanNumber", "Location")

	name := "-"
	for _, publicVlan := range publicVlans {
		if publicVlan.Name != nil {
			name = *publicVlan.Name
		}
		fmt.Printf("| %10d ", *publicVlan.Id)
		fmt.Printf("| %20s ", name)
		fmt.Printf("| %20d ", *publicVlan.VlanNumber)
		fmt.Printf("| %20s |\n", *publicVlan.BillingItem.Location.LongName)
	}

	objFilterPrivate := filter.Path("privateNetworkVlans.billingItem.location.id").Eq(locationId).Build()

	privateVlans, err := accountServer.Mask(objMask).Filter(objFilterPrivate).GetPrivateNetworkVlans()
	if err != nil {
		fmt.Printf("Unable to retrieve the privateVlans: %s\n", err)
		os.Exit(1)
	}

	fmt.Println()
	fmt.Println("---------------------------------- PRIVATE VLANS ----------------------------------")

	fmt.Printf("| %10s | %20s |%20s |%20s | \n", "Id", "Name", "VlanNumber", "Location")
	for _, privateVlan := range privateVlans {
		fmt.Printf("| %10d ", *privateVlan.Id)
		fmt.Printf("| %20s ", *privateVlan.Name)
		fmt.Printf("| %20d ", *privateVlan.VlanNumber)
		fmt.Printf("| %20s |\n", *privateVlan.BillingItem.Location.LongName)
	}
}

func ListAvailableRouters(locationId int) {
	objFilter := filter.Path("routers.topLevelLocation.id").Eq(locationId).Build()

	routers, err := accountServer.Filter(objFilter).GetRouters()
	if err != nil {
		fmt.Printf("Unable to retrieve the routers: %s\n", err)
		os.Exit(1)
	}

	fmt.Printf("| %10s | %20s |%20s | \n", "Id", "Hostname", "Location")
	for _, router := range routers {
		fmt.Printf("| %10d ", *router.Id)
		fmt.Printf("| %20s ", *router.Hostname)
		fmt.Printf("| %20s| \n", *router.TopLevelLocation.LongName)
	}
}

```

### Order a Virtual Server by backend/frontend vlan ids.

1. Find the package that you want to order. listServerPackages() will filter out all VIRTUAL_SERVER_INSTANCE.

2. Use getServerPrices() to find the item keyNames you want to include in your order. These price IDs can be 
    included prices array directly, but I’ve included gatherPriceIds() to match up KeyNames to build a list of price 
    ids. getServerPrices() will also show the locations available for ordering.

3. listActivePresets() will list all active presets for a specific package.

4. listAvailableVlans() if you want to place the server on a specific VLAN.

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"

	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

// Create the session and services
var sess = session.New()
var packageService = services.GetProductPackageService(sess)
var orderService = services.GetProductOrderService(sess)
var accountServer = services.GetAccountService(sess)

// Parameters will help us to reduce the number of argument in a function.
type Parameters struct {
	hostname  string
	domain    string
	packageId int
	hourly    bool
	location  string
	items     []string
	backend   int
	frontend  int
	flavor    int
}

func main() {
	/**
	Step 1, find the package server type you want
	e.g. 835  PUBLIC_CLOUD_SERVER

	Remove the comment '//' below to get the 'listServerPackages()' information.
	*/

	//ListServerPackage()
	packageId := 835

	/**
	Step 2, Collect all the pieces you want to order
	getServerPrices will list out all the keyNames and cost of components
	that can be ordered on a certain package. Will also list the DCs that this
	server is available in.

	Remove the comment '//' below to 'getServerPrices()' information.
	*/

	//GetServerPrices(packageId)
	//locationId := 138124

	/**
	Step 3, will list all active presets.

	Remove the comment '//' below to 'getServerPrices()' information.
	*/

	//ListActivePresets(packageId)
	presetId := 345

	/**
	Step 4, Will list all available public and private vlans.

	Remove the comment '//' below to 'listAvailableVlans()' information.
	*/

	//ListAvailableVlans(locationId)
	pubVlanId := 1111
	privVlanId := 2222

	/**
	Step 5, Order a virtual server by backend/frontend vlan.

	Remove the comment '//' below to order a bare metal server.
	*/

	locationKeyName := "DALLAS05"

	OrderVirtualServer(packageId, locationKeyName, presetId, pubVlanId, privVlanId)

}

func OrderVirtualServer(packageId int, locationKeyName string, flavor int, frontend int, backend int) {
	// KeyNames of the items
	items := []string{
		"1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS",
		"BANDWIDTH_0_GB_2",
		"1_IP_ADDRESS",
		"OS_UBUNTU_16_04_LTS_XENIAL_XERUS_MINIMAL_64_BIT_FOR_VSI",
		"REBOOT_REMOTE_CONSOLE",
		"MONITORING_HOST_PING",
		"NOTIFICATION_EMAIL_AND_TICKET",
		"AUTOMATED_NOTIFICATION",
		"UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT",
	}

	parameters := Parameters{
		hostname:  "myhostname",
		domain:    "domain.com",
		backend:   backend,
		frontend:  frontend,
		items:     items,
		location:  locationKeyName,
		packageId: packageId,
		flavor:    flavor,
		hourly:    true,
	}

	prices := GetPrices(packageId, items)

	// Build the Virtual Server array object.
	virtualGuests := BuildArrayVirtualServer(parameters)

	// Build the Container_Product_Order with the basic required data
	containerOrder := datatypes.Container_Product_Order{
		PackageId:        sl.Int(parameters.packageId),
		Location:         sl.String(parameters.location),
		VirtualGuests:    virtualGuests,
		Prices:           prices,
		UseHourlyPricing: sl.Bool(parameters.hourly),
	}
	// Add presetId to the Container_Product_Order if a flavor exists
	if parameters.flavor > 0 {
		containerOrder.PresetId = &flavor
	}

	// Build the order template that will be used to order the virtual server
	orderTemplate := datatypes.Container_Product_Order_Virtual_Guest{
		Container_Product_Order_Hardware_Server: datatypes.Container_Product_Order_Hardware_Server{
			Container_Product_Order: containerOrder,
		},
	}

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := orderService.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("Unable to verify/place the order: %s", err)
	}

	// pretty print
	jsonFormat, jsonErr := json.MarshalIndent(receipt, "", "   ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	fmt.Println(string(jsonFormat))
}

func GetServerPrices(packageID int) {
	mask := "mask[regions,items[prices],activeServerItems[prices]]"
	result, err := packageService.Mask(mask).Id(packageID).GetObject()
	if err != nil {
		fmt.Printf("Unable to retrieve items: %s\n", err)
		os.Exit(1)
	}

	fmt.Println("---------------- Locations -------------------")
	fmt.Printf("| %10s | %20s |\n", "Location Id", "Location Name")
	for _, location := range result.Regions {
		fmt.Printf("| %10d ", *location.Location.Location.Id)
		fmt.Printf("| %20s |\n", *location.Description)
	}

	cores := "-"
	recurringFee := 0.0
	fmt.Println("----------------------------------------- Item Prices ------------------------------------------")
	fmt.Printf("| %10s | %50s | %10s | %10s | %40s |\n", "Price Id", "Description", "Cores", "Monthly Fee", "KeyName")
	for _, item := range result.Items {
		for _, price := range item.Prices {
			if price.LocationGroupId == nil {
				if price.RecurringFee != nil {
					recurringFee = float64(*price.RecurringFee)
				}
				if price.CapacityRestrictionType != nil {
					cores = fmt.Sprintf("%s - %s", *price.CapacityRestrictionMinimum, *price.CapacityRestrictionMaximum)

					fmt.Printf("| %10d ", *price.Id)
					fmt.Printf("| %50s ", *item.Description)
					fmt.Printf("| %10s ", cores)
					fmt.Printf("| %10f ", recurringFee)
					fmt.Printf("| %40s |\n", *item.KeyName)
				} else {
					fmt.Printf("| %10d ", *price.Id)
					fmt.Printf("| %50s ", *item.Description)
					fmt.Printf("| %10s ", cores)
					fmt.Printf("| %10f ", recurringFee)
					fmt.Printf("| %40s |\n", *item.KeyName)
				}
			}
		}
	}
}

func ListServerPackage() {
	objFilter := filter.Path("type.keyName").Eq("VIRTUAL_SERVER_INSTANCE").Build()
	packages, err := packageService.Mask("mask[type]").Filter(objFilter).GetAllObjects()
	if err != nil {
		fmt.Printf("Package %s doesn't exists\n", "VIRTUAL_SERVER_INSTANCE")
		os.Exit(1)
	}
	fmt.Printf("| %10s | %45s | %45s | %20s |\n", "Id", "Name", "KeyName", "Type")
	for _, item := range packages {
		fmt.Printf("| %10d ", *item.Id)
		fmt.Printf("| %45s ", *item.Name)
		fmt.Printf("| %45s ", *item.KeyName)
		fmt.Printf("| %20s |\n", *item.Type.KeyName)
	}
}

// GetPrices returns the list of prices.
func GetPrices(packageID int, itemKeyNames []string) []datatypes.Product_Item_Price {
	objMask := "mask[id,itemCategory,keyName,prices[categories]]"

	items, err := packageService.Mask(objMask).Id(packageID).GetItems()
	if err != nil {
		fmt.Printf("Unable to retrieve items: %s\n", err)
		os.Exit(1)
	}

	prices := make([]datatypes.Product_Item_Price, len(itemKeyNames))

	for idx, itemKeyName := range itemKeyNames {
		prices[idx].Id, err = GetPriceIDIfMatch(itemKeyName, items)
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
	}

	return prices
}

// GetPriceIDIfMatch returns a priceID or error if keyName doesnt exists.
func GetPriceIDIfMatch(keyName string, items []datatypes.Product_Item) (priceID *int, err error) {
	var matchingItem datatypes.Product_Item
	// find the item keyname
	for _, item := range items {
		if keyName == *item.KeyName {
			matchingItem = item
			break
		}
	}
	// returns error if keyName doesn't exists in the items list
	if matchingItem.KeyName == nil {
		return nil, fmt.Errorf("The item %s doesn't exists in the package", keyName)
	}
	// find the standard priceID
	for _, price := range matchingItem.Prices {
		if price.LocationGroupId == nil {
			priceID = price.Id
			break
		}
	}

	return
}

// BuildArrayVirtualServer builds the esqueleton of Virtual Server array.
func BuildArrayVirtualServer(args Parameters) []datatypes.Virtual_Guest {
	virtualGuests := []datatypes.Virtual_Guest{
		{
			Hostname: sl.String(args.hostname),
			Domain:   sl.String(args.domain),
		},
	}

	if args.backend > 0 {
		virtualGuests[0].PrimaryBackendNetworkComponent = &datatypes.Virtual_Guest_Network_Component{
			NetworkVlan: &datatypes.Network_Vlan{
				Id: sl.Int(args.backend),
			},
		}
	}

	if args.frontend > 0 {
		virtualGuests[0].PrimaryNetworkComponent = &datatypes.Virtual_Guest_Network_Component{
			NetworkVlan: &datatypes.Network_Vlan{
				Id: sl.Int(args.frontend),
			},
		}
	}

	return virtualGuests
}

func ListAvailableVlans(locationId int) {
	objMask := "mask[billingItem[location]]"
	objFilter := filter.Path("publicNetworkVlans.billingItem.location.id").Eq(locationId).Build()

	publicVlans, err := accountServer.Mask(objMask).Filter(objFilter).GetPublicNetworkVlans()
	if err != nil {
		fmt.Printf("Unable to retrieve the publicVlans: %s\n", err)
		os.Exit(1)
	}

	fmt.Println("---------------------------------- PUBLIC VLANS ---------------------------------------")

	fmt.Printf("| %10s | %20s |%20s |%20s | \n", "Id", "Name", "VlanNumber", "Location")

	name := "-"
	for _, publicVlan := range publicVlans {
		if publicVlan.Name != nil {
			name = *publicVlan.Name
		}
		fmt.Printf("| %10d ", *publicVlan.Id)
		fmt.Printf("| %20s ", name)
		fmt.Printf("| %20d ", *publicVlan.VlanNumber)
		fmt.Printf("| %20s |\n", *publicVlan.BillingItem.Location.LongName)
	}

	objFilterPrivate := filter.Path("privateNetworkVlans.billingItem.location.id").Eq(locationId).Build()

	privateVlans, err := accountServer.Mask(objMask).Filter(objFilterPrivate).GetPrivateNetworkVlans()
	if err != nil {
		fmt.Printf("Unable to retrieve the privateVlans: %s\n", err)
		os.Exit(1)
	}

	fmt.Println()
	fmt.Println("---------------------------------- PRIVATE VLANS ----------------------------------")

	fmt.Printf("| %10s | %20s |%20s |%20s | \n", "Id", "Name", "VlanNumber", "Location")
	for _, privateVlan := range privateVlans {
		fmt.Printf("| %10d ", *privateVlan.Id)
		fmt.Printf("| %20s ", *privateVlan.Name)
		fmt.Printf("| %20d ", *privateVlan.VlanNumber)
		fmt.Printf("| %20s |\n", *privateVlan.BillingItem.Location.LongName)
	}
}

func ListAvailableRouters(locationId int) {
	objFilter := filter.Path("routers.topLevelLocation.id").Eq(locationId).Build()

	routers, err := accountServer.Filter(objFilter).GetRouters()
	if err != nil {
		fmt.Printf("Unable to retrieve the routers: %s\n", err)
		os.Exit(1)
	}

	fmt.Printf("| %10s | %20s |%20s | \n", "Id", "Hostname", "Location")
	for _, router := range routers {
		fmt.Printf("| %10d ", *router.Id)
		fmt.Printf("| %20s ", *router.Hostname)
		fmt.Printf("| %20s| \n", *router.TopLevelLocation.LongName)
	}
}

func ListActivePresets(packageId int) {
	active_presets, err := packageService.Id(packageId).GetActivePresets()
	if err != nil {
		fmt.Printf("Unable to retrieve the active presets: %s\n", err)
		os.Exit(1)
	}

	fmt.Printf("| %10s | %20s |%20s | \n", "Id", "Description", "KeyName")
	for _, preset := range active_presets {
		fmt.Printf("| %10d ", *preset.Id)
		fmt.Printf("| %20s ", *preset.Description)
		fmt.Printf("| %20s| \n", *preset.KeyName)
	}
}

```