---
title: "order_server_with_raid_configuration.go"
description: "order_server_with_raid_configuration.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Storage_Group"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```go
/*
Order server with RAID configuration.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder

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
  	username    := "set me"
  	apikey      := "set me"

	// Declare the complexType, location, packageId and quantity for the server
	// you wish to order
  	quantity    := 1
  	hostname    := "softlayer"
  	domain      := "example.com"
  	location    := "AMSTERDAM"
  	packageId   := 265          // Dual E5-2600 Series (12 Drives)

	// Build array of SoftLayer_Hardware objects
  	hardware := []datatypes.Hardware {
		{	// Hostname and domain of SoftLayer_Hardware object
			Hostname : sl.String(hostname),
      			Domain   : sl.String(domain),
    		},
  	}

	// Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
	// prices for the package use the SoftLayer_Product_Package:getItems method
  	prices := []datatypes.Product_Item_Price {
    		{ Id: sl.Int(180149) },     // Dual Intel Xeon E5-2690 (8 Cores, 2.90 GHz)
    		{ Id: sl.Int( 74095) },     // 16 GB
    		{ Id: sl.Int( 44988) },     // CentOS 7.x (64 bit)
    		{ Id: sl.Int( 75005) },     // RAID
    		{ Id: sl.Int( 68789) },     // 500 GB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 64817) },     // 1.00 TB SATA
    		{ Id: sl.Int( 50357) },     // 500 GB Bandwidth
    		{ Id: sl.Int(   273) },     // 100 Mbps Public & Private Network Uplinks
    		{ Id: sl.Int( 76205) },     // Redundant Power Supply
    		{ Id: sl.Int(    55) },     // Host Ping
    		{ Id: sl.Int(    58) },     // Automated Notification
    		{ Id: sl.Int(   420) },     // Unlimited SSL VPN Users & 1 PPTP VPN User per account
    		{ Id: sl.Int(   418) },     // Nessus Vulnerability Assessment & Reporting
    		{ Id: sl.Int(    21) },     // 1 IP Address
    		{ Id: sl.Int(    57) },     // Email and Ticket
    		{ Id: sl.Int(   906) },     // Reboot / KVM over IP
  	}

	// Building a skeleton SoftLayer_Container_Product_Order_Storage_Group object
	// Storage groups will only be used if the 'RAID' disk controller price is selected.
	// Any other disk controller types will ignore the storage groups set here.
	// The first storage group in this array will be considered the primary storage group,
	// which is used for the OS. Any other storage groups will act as data storage.
  	storageGroups := []datatypes.Container_Product_Order_Storage_Group {
	    	{ 	// First Container_Product_Order_Storage_Group object
      			ArraySize           : sl.Float(1998),
      			ArrayTypeId         : sl.Int(3),     // RAID_5
      			HardDrives          : []int{ 1, 2, 3, 4 },
      			PartitionTemplateId : sl.Int(6),
    		},
		{	// Second Container_Product_Order_Storage_Group object
      			ArraySize           : sl.Float(500),
      			ArrayTypeId         : sl.Int(9),
      			HardDrives          : []int{ 0 },
			// The custom partitions only works for other storage groups
			// different from the primary one
      			Partitions          : []datatypes.Container_Product_Order_Storage_Group_Partition{
        			{	// First Container_Product_Order_Storage_Group_Partition
          				IsGrow : sl.Bool(false),
          				Name   : sl.String("/diskC"),
          				Size   : sl.Float(100),
        			},
        			{	// Second Container_Product_Order_Storage_Group_Partition
          				IsGrow : sl.Bool(true),
          				Name   : sl.String("/diskD"),
          				Size   : sl.Float(200),
        			},
      			},
    		},
    		{	// Third Container_Product_Order_Storage_Group object
      			ArraySize           : sl.Float(2264),
      			ArrayTypeId         : sl.Int(1),     // RAID_0
      			HardDrives          : []int{ 5, 6, 7, 8 },
      			Partitions          : []datatypes.Container_Product_Order_Storage_Group_Partition{
        			{	// Third Container_Product_Order_Storage_Group_Partition
          				IsGrow : sl.Bool(false),
          				Name   : sl.String("/diskA"),
          				Size   : sl.Float(500),
        			},
        			{	// Fourth Container_Product_Order_Storage_Group_Partition
          				IsGrow : sl.Bool(true),
          				Name   : sl.String("/diskB"),
          				Size   : sl.Float(200),
        			},
      			},
    		},
  	}

  	// Build the skeleton of SoftLayer_Container_Product_Order object
	// containing the order you wish to place.
	orderTemplate := datatypes.Container_Product_Order {
		Quantity      :	sl.Int(quantity),
		Location      : sl.String(location),
		PackageId     : sl.Int(packageId),
		Hardware      : hardware,
		Prices        : prices,
		StorageGroups : storageGroups,
	}

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Product_Order service
	service := services.GetProductOrderService(sess)

	// Use verifyOrder() method to check for errors. Replace this with placeOrder() when
	// you are ready to order.
	receipt, err := service.VerifyOrder(&orderTemplate)
	if err != nil {
		fmt.Printf("\n Unable to place/verify order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat, jsonErr := json.MarshalIndent(receipt,"","    ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
		return
	}

	fmt.Println(string(jsonFormat))
}

```
