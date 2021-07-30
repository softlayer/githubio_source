---
title: "More Bare Metal Server examples"
description: "Working with Bare Metal Server"
date: "2021-07-12"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Hardware_Server"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
    - "hardware"
    - "order"
    - "objectfilter"
    - "objectmask"
---

A few examples on interacting with Bare Metal Server, [SoftLayer_Hardware_Server](https://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/).

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/IBM-Cloud/ibm-cloud-cli-sdk/bluemix/terminal"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

// Session created using values set in the environment, or from the local configuration file (i.e. ~/.softlayer).
var sess = session.New()

type Dictionary map[string]string

func main() {

	// Shows all servers in the account.
	listServers()

	// Shows all available packages to order/create a Bare Metal server.
	listServerPackages()

	// Shows just fast provision packages to order/create a Bare Metal server.
	listServerPackagesFastProvision()

	// Shows available locations for the package and the items within the package.
	packageKeyname := "DUAL_E52600_V4_12_DRIVES"
	listPackageDetails(packageKeyname)

	// Function to create a hardware server, it contains an example that could use as a template,
	// so changing the values within the example we can order a different server,
	// the functions provided above,
	// helps to get all available values to build an order for Bare Metal Server.
	serverCreate()

	//Shows some details for a Bare Metal Server.
	hostname := "server-hostname"
	serverDetails(hostname)

	// Edit some parameters for a server, just uncomment hostname and domain if you want to update them.
	paramsToEdit := Dictionary{
		"Notes": "My golang note",
		//"Hostaname": "NewHostname",
		//"Domain": "NewDomain",
	}

	hostname = "server-hostname"
	editServer(hostname, paramsToEdit)

	// Cancel a bare metal server.
	// To make sure the server specified to cancel is the one you want
	// verify that the identifier passed to cancelServer is correct.
	hostname = "server-hostname-to-cancel"
	serverId := getServerId(hostname)
	cancelServer(serverId)
}

/**
Creates a hardware server, it contains an example to build an order for a Bare Metal Server.
*/
func serverCreate() {

	quantity := 1
	location := "TORONTO"

	// listServerPackages() shows all available package IDs as well as their key names.
	packageId := 553
	hostname := "test"
	domain := "example.com"

	server := []datatypes.Hardware{
		{
			Hostname: sl.String(hostname),
			Domain:   sl.String(domain),
		},
	}

	required_items := []string{
		"AUTOMATED_NOTIFICATION",
		"MONITORING_HOST_PING",
		"NOTIFICATION_EMAIL_AND_TICKET",
		"REBOOT_KVM_OVER_IP",
		"UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT",
		"REDUNDANT_POWER_SUPPLY",
	}
	//We need bandwidth, at least 1 ip, and the port speed.
	network_items := []string{
		"BANDWIDTH_500_GB",
		"1_IP_ADDRESS",
		"1_GBPS_DUAL_PUBLIC_PRIVATE_NETWORK_UPLINKS_UNBONDED",
	}
	//A disk controller, a duplicate entry for each disk you want, in order, ram, OS and processor chip.
	physical_items := []string{
		"DISK_CONTROLLER_RAID",
		"HARD_DRIVE_2_00_TB_SATA_2",
		"HARD_DRIVE_2_00_TB_SATA_2",
		"HARD_DRIVE_2_00_TB_SATA_2",
		"HARD_DRIVE_12_00_TB_SATA",
		"RAM_64_GB_DDR4_2133_ECC_NON_REG",
		"OS_CENTOS_7_X_64_BIT",
		"INTEL_INTEL_XEON_E52620_V4_2_10",
		"HARD_DRIVE_NVME_375_GB_PCIE",
	}

	orderItems := append(network_items, required_items...)
	orderItems = append(orderItems, physical_items...)
	// Build a skeleton SoftLayer_Product_Item_Price objects.
	prices := getItemPriceList(packageId, orderItems)

	// Build a container_Product_Order object.
	orderTemplate := datatypes.Container_Product_Order{
		Quantity:  sl.Int(quantity),
		Location:  sl.String(location),
		PackageId: sl.Int(packageId),
		Prices:    prices,
		Hardware:  server,
	}
	// Get SoftLayer_Product_Order service.
	service := services.GetProductOrderService(sess)

	/* Use verifyOrder() method to check for errors.
	   Replace this with placeOrder() when you are ready to order.
	*/
	result, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}
	printAsJsonFormat(result)

}

/**
Converts a list of item keyNames to a list of standard item prices,
given package associated with the prices and a list of items KeyNames.
*/
func getItemPriceList(packageId int, itemKeyNames []string) (resp []datatypes.Product_Item_Price) {

	items := getPackageItems(packageId)
	var prices []datatypes.Product_Item_Price

	for _, itemKeyName := range itemKeyNames {
		for _, item := range items {
			if (*item.KeyName) == itemKeyName {
				itemPrice := getStandardPrice(item)
				prices = append(prices, itemPrice)
				break

			}
		}
	}

	return prices
}

//Gets the items for the given package identifier.
func getPackageItems(packageId int) (resp []datatypes.Product_Item) {
	var mask = "id, itemCategory, keyName," +
		"prices[id, hourlyRecurringFee, recurringFee, categories]"
	var service = services.GetProductPackageService(sess)
	receipt, err := service.Id(packageId).Mask(mask).GetItems()
	if err != nil {
		fmt.Printf("\n Unable to get Items:\n - %s\n", err)
		return
	}

	return receipt
}

/**
Prints the items and locations available in the given package
*/
func listPackageDetails(keyname string) {

	// Get SoftLayer_Product_Package service
	service := services.GetProductPackageService(sess)
	filter := filter.Build(
		filter.Path("keyName").
			Eq(keyname),
	)
	mask := "id, keyName, description, regions," +
		"items[id, keyName, description," +
		"prices[hourlyRecurringFee, recurringFee," +
		"capacityRestrictionMaximum, capacityRestrictionMinimum, capacityRestrictionType]]"
	// Call the method SoftLayer_Product_Package:getAllObjects
	packages, err := service.Filter(filter).Mask(mask).GetAllObjects()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	productPackage := packages[0]
	printLocations(productPackage)
	printItemsDetails(productPackage.Items)

}

/**
Prints the locations for a Product_Package.
*/
func printLocations(packageInstance datatypes.Product_Package) {
	rows := []string{
		"Locations",
	}
	cmd := terminal.NewStdUI()
	table := cmd.Table(rows)
	for _, region := range packageInstance.Regions {
		keyname := sl.Get(region.Keyname).(string)
		table.Add(keyname)
	}
	cmd.Say("List of Locations")
	table.Print()
}

/**
Prints a list of product items.
*/
func printItemsDetails(items []datatypes.Product_Item) {
	rows := []string{
		"Keyname",
		"restriction _ minimum _ maximum",
		"standard_monthly_price",
		"standard_hourly_price",
	}
	cmd := terminal.NewStdUI()
	table := cmd.Table(rows)
	for _, item := range items {
		itemPrice := getStandardPrice(item)
		keyname := sl.Get(item.KeyName).(string)
		capacityRestrictionType := sl.Get(itemPrice.CapacityRestrictionType).(string)
		capacityRestrictionMinimum := sl.Get(itemPrice.CapacityRestrictionMinimum).(string)
		capacityRestrictionMaximum := sl.Get(itemPrice.CapacityRestrictionMaximum).(string)
		restriction := fmt.Sprintf("%s _ %s _ %s",
			capacityRestrictionType,
			capacityRestrictionMinimum,
			capacityRestrictionMaximum)
		hourly := true
		hourlyPrice := sl.Get(getFee(item, hourly)).(string)
		hourly = false
		monthlyPrice := sl.Get(getFee(item, hourly)).(string)
		table.Add(keyname, restriction, monthlyPrice, hourlyPrice)
	}
	cmd.Say("List of product items")
	table.Print()
}

/**
Gets the HourlyRecurringFee or monthly RecurringFee from a Product_Item_Price.
*/
func getFee(item datatypes.Product_Item, hourlyPriceFlag bool) (resp string) {

	itemPrice := getStandardPrice(item)

	if itemPrice.HourlyRecurringFee != nil && hourlyPriceFlag {
		return fmt.Sprintf("%.2f", *itemPrice.HourlyRecurringFee)
	}

	if itemPrice.RecurringFee != nil && !hourlyPriceFlag {
		return fmt.Sprintf("%.2f", *itemPrice.RecurringFee)
	}
	return "_"
}

/**
Gets the standard Price from an item.
*/
func getStandardPrice(item datatypes.Product_Item) (resp datatypes.Product_Item_Price) {
	for _, itemPrice := range item.Prices {
		if itemPrice.LocationGroupId == nil {
			return itemPrice
		}
	}
	return datatypes.Product_Item_Price{}

}

/**
Prints the servers in the account.
*/
func listServers() {

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Object-Mask in order to get specific data of server.
	mask := "id;hostname;primaryIpAddress;primaryBackendIpAddress;datacenter;" +
		"datacenterName;serviceProvider;hardwareFunctionDescription"

	// Call the getHardware() method.
	hardware, err := service.Mask(mask).GetHardware()
	if err != nil {
		fmt.Printf("\n Unable to get Bare Metal Servers:\n - %s\n", err)
		return
	}
	printServers(hardware)

}

/**
Prints a list of servers
*/
func printServers(servers []datatypes.Hardware) {
	rows := []string{"id", "hostname", "primary_ip", "backend_ip", "datacenter"}
	cmd := terminal.NewStdUI()
	table := cmd.Table(rows)
	for _, server := range servers {
		serverId := fmt.Sprintf("%d", server.Id)
		hostname := sl.Get(server.Hostname).(string)
		primaryIp := sl.Get(server.PrimaryIpAddress).(string)
		backendIp := sl.Get(server.PrimaryBackendIpAddress).(string)
		datacenter := sl.Get(server.DatacenterName).(string)

		table.Add(serverId, hostname, primaryIp, backendIp, datacenter)
	}
	cmd.Say("List of Servers")
	table.Print()
}

/**
Prints the available Bare Metal Servers packages.
*/
func listServerPackages() {

	// Get SoftLayer_Product_Package_Server service
	service := services.GetProductPackageServerService(sess)

	// To get all packages of servers available for ordering, we will use the following filter.
	filter := filter.Build(
		filter.Path("packageType").
			In("BARE_METAL_CORE", "BARE_METAL_CPU", "BARE_METAL_CPU_FAST_PROVISION"),
	)
	mask := "package"
	// Call the method SoftLayer_Product_Package_Server::getAllObjects
	productPackageServes, err := service.Filter(filter).Mask(mask).GetAllObjects()
	//productPackageServes, err := service.GetAllObjects()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	printPackageDetails(productPackageServes)

}

/**
Prints the available Bare Metal Servers packages BARE_METAL_CPU_FAST_PROVISION type.
*/
func listServerPackagesFastProvision() {

	// Get SoftLayer_Product_Package_Server service
	service := services.GetProductPackageServerService(sess)

	// In order to get all 'BARE_METAL_CPU_FAST_PROVISION' servers to order we will use the following filter
	filter := filter.Build(
		filter.Path("packageType").Eq("BARE_METAL_CPU_FAST_PROVISION"),
	)

	mask := "package"
	// Call the method SoftLayer_Product_Package_Server::getAllObjects
	productPackageServes, err := service.Filter(filter).Mask(mask).GetAllObjects()
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	printPackageDetails(productPackageServes)
}

/**
Prints the package details.
*/
func printPackageDetails(productPackages []datatypes.Product_Package_Server) {
	rows := []string{"id", "keyname", "description"}
	cmd := terminal.NewStdUI()
	table := cmd.Table(rows)
	for _, productPackage := range productPackages {
		id := fmt.Sprintf("%d", *productPackage.PackageId)
		keyname := sl.Get(productPackage.Package.KeyName).(string)
		name := sl.Get(productPackage.ProductName).(string)

		table.Add(id, keyname, name)
	}
	cmd.Say("Package details")
	table.Print()
}

/**
Edit note, hostname, and domain of a hardware server
*/
func editServer(serverName string, params Dictionary) {

	// Define the new local properties to set. While we're only editing a server's notes
	// in this example you can also use editObject() to edit the server's hostname and domain.
	objectTemplate := datatypes.Hardware_Server{}

	if notes, ok := params["Notes"]; ok {
		objectTemplate.Notes = sl.String(notes)
	}
	if hostname, ok := params["Hostname"]; ok {
		objectTemplate.Notes = sl.String(hostname)
	}
	if domain, ok := params["Domain"]; ok {
		objectTemplate.Notes = sl.String(domain)
	}

	hardwareService := services.GetHardwareServerService(sess)
	serverId := getServerId(serverName)

	result, err := hardwareService.Id(serverId).EditObject(&objectTemplate)
	if err != nil {
		fmt.Printf("\n Unable to edit the server '"+serverName+"'\n - %s\n", err)
		return
	}

	if result {
		fmt.Printf("\n Server '%s' was successfuly edited\n", serverName)
		serverDetails(serverId)
	}

}

/**
Prints server details by server identifier
*/
func serverDetails(identifier interface{}) {
	serverId := 0
	switch identifier := identifier.(type) {
	case int:
		serverId = identifier
	case string:
		hostname := identifier
		serverId = getServerId(hostname)
	}

	mask := "id, hostname, domain, globalIdentifier, fullyQualifiedDomainName, hardwareStatus," +
		"processorPhysicalCoreAmount, memoryCapacity, primaryBackendIpAddress, primaryIpAddress," +
		"networkManagementIpAddress, datacenter," +
		"operatingSystem[softwareLicense[softwareDescription[manufacturer, name, version, referenceCode]]]," +
		"billingItem[id, nextInvoiceTotalRecurringAmount, children[nextInvoiceTotalRecurringAmount]," +
		"orderItem.order.userRecord[username]], tagReferences[id, tag[name, id]], notes"

	server := getServerIntance(serverId, mask)
	printServerDetail(server)
}

/**
Gets the identifier of a server from the hostname.
*/
func getServerId(hostname string) (resp int) {
	accountService := services.GetAccountService(sess)
	// Following filter and mask helps to get the ID of bare metal server
	filter := filter.Build(filter.Path("hardware.hostname").Eq(hostname))
	mask := "id;hostname"

	// Call the getHardware() method to get list of servers that matches with the filter
	hardware, err := accountService.Mask(mask).Filter(filter).GetHardware()
	if err != nil {
		fmt.Printf("\n Unable to find server '"+hostname+"'\n - %s\n", err)
		return
	}

	// If server name was not found we throw a message
	if len(hardware) < 1 {
		fmt.Printf("\n Unable to find server '%s'\n", hostname)
	}
	return *hardware[0].Id
}

/**
Prints server details
*/
func printServerDetail(server datatypes.Hardware_Server) {
	rows := []string{"Name", "Value"}
	cmd := terminal.NewStdUI()
	table := cmd.Table(rows)
	table.Add("ID", fmt.Sprintf("%d", *server.Id))
	table.Add("GUID", sl.Get(server.GlobalIdentifier).(string))
	table.Add("Hostname", sl.Get(server.Hostname).(string))
	table.Add("Domain", sl.Get(server.Domain).(string))
	table.Add("FQDN", sl.Get(server.FullyQualifiedDomainName).(string))
	if server.HardwareStatus != nil {
		table.Add("Status", sl.Get(server.HardwareStatus.Status).(string))
	}
	if server.Datacenter != nil {
		table.Add("Datacenter", sl.Get(server.Datacenter.Name).(string))
	}
	table.Add("CPU cores", fmt.Sprintf("%d", *server.ProcessorPhysicalCoreAmount))
	table.Add("Memory", (fmt.Sprintf("%d", *server.MemoryCapacity) + "GB"))
	table.Add("Public IP", sl.Get(server.PrimaryIpAddress).(string))
	table.Add("Private IP", sl.Get(server.PrimaryBackendIpAddress).(string))
	table.Add("IPMI IP", sl.Get(server.NetworkManagementIpAddress).(string))
	if server.OperatingSystem != nil &&
		server.OperatingSystem.SoftwareLicense != nil &&
		server.OperatingSystem.SoftwareLicense.SoftwareDescription != nil {
		table.Add("OS",
			sl.Get(server.OperatingSystem.SoftwareLicense.SoftwareDescription.Name).(string))
		table.Add("OS version",
			sl.Get(server.OperatingSystem.SoftwareLicense.SoftwareDescription.Version).(string))
	}
	if server.Notes != nil && *server.Notes != "" {
		table.Add("Note", sl.Get(server.Notes).(string))
	}
	cmd.Say("Server details")
	table.Print()
}

/**
Prints the data as format JSON.
*/
func printAsJsonFormat(data interface{}) {
	jsonData, jsonErr := json.MarshalIndent(data, "", "    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}
	println(string(jsonData))
}

/*
Cancel a bare metal server.
The server will be canceled immediately if it is billed Hourly,
for the Monthly server, the cancellation will be made after the next bill date.
*/

func cancelServer(serverId int) {

	// In order to cancel billing item of server we need to set following values
	cancelAssociatedBillingItems := false
	reason := "No longer needed"
	customerNote := "BMS - canceled"

	// Get SoftLayer_Billing_Item service
	billingService := services.GetBillingItemService(sess)
	mask := "id;hostname;billingItem;hourlyBillingFlag"
	server := getServerIntance(serverId, mask)

	// If server is billed hourly it will be canceled immediately, for monthly server
	// the cancellation will be made after next bill date.
	cancelImmediately := server.HourlyBillingFlag

	// Call the cancelItem() method in order to cancel the bare metal server
	result, err := billingService.Id(*server.BillingItem.Id).CancelItem(cancelImmediately,
		&cancelAssociatedBillingItems, &reason, &customerNote)
	if err != nil {
		fmt.Printf("\n Unable to cancel the server '%d' \n - %s\n", serverId, err)
		return
	}

	// Print final result
	if result {
		fmt.Printf("\n Server '%d' was successfuly cancelled\n", serverId)
	} else {
		fmt.Printf("\n Server '%d' could not be cancelled\n", serverId)
	}

}

//Gets the server instance by identifier using a specific object mask.
func getServerIntance(serverId int, mask string) (resp datatypes.Hardware_Server) {

	hardwareService := services.GetHardwareServerService(sess)
	server, err := hardwareService.Id(serverId).Mask(mask).GetObject()
	if err != nil {
		fmt.Printf("\n Unable to get server \n - %s\n", err)
		return
	}
	return server

}

```