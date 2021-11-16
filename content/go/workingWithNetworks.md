---
title: "Working with VLANs"
description: "A collection of CLI Examples on how to interact with VLANs."
date: "2021-09-29"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_VLan"
    - "SoftLayer_Network_Subnet"
tags:
    - "subnet"
    - "vlan"
    - "network"
---

For these set of examples, we will be using a [cobra](https://github.com/spf13/cobra) CLI framework for golang, letting us create an individual command for each example as we go along. Read up on the [Golang Example Framework](/go/exampleFramework) for information on how to setup the CLI Framework to get this code to run easily.


## Listing VLANs

Listing vlans is likely the most common thing to do, so it makes a good starting point. This script makes a paginated API call to [SoftLayer_Account::getNetworkVlans()](/reference/services/SoftLayer_Account/getNetworkVlans/) and prints out a quick CSV about the servers on your acccount.

>github.com/softlayer/softlayer-go/examples/cmd/vlan_list.go

```go
package cmd

import (
    "fmt"

    "github.com/spf13/cobra"

    "github.com/softlayer/softlayer-go/filter"
    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
)

func init() {
    listVlanCmd.Flags().StringVarP(&Datacenter, "datacenter", "d", "", "List only VLANs from this datacenter")
    listVlanCmd.Flags().BoolVarP(&Firewall, "firewall", "", false, "List only VLANs with a dedicated firewall")
    rootCmd.AddCommand(listVlanCmd)
}

var Datacenter string
var Firewall bool
var listVlanCmd = &cobra.Command{
    Use:   "vlan-list",
    Short: "Lists all vlans on the account",
    Long:  `Lists all vlans on the account`,
    RunE: func(cmd *cobra.Command, args []string) error {
        return VlanListCommand(cmd, args)
    },
}



func VlanListCommand(cmd *cobra.Command, args []string) error {
    resultLimit := 50
    resultOffset := 0
    objectMask := "mask[id,name,vlanNumber,primaryRouter[id,hostname,datacenterName,datacenter[name]]]"
    // When using a result Limit to break up your API request, its important to include an orderBy objectFilter
    // to enforce an order on the query, as the database might not always return results in the same order between
    // queries otherwise
    filters := filter.New()
    filters = append(filters, filter.Path("networkVlans.id").OrderBy("DESC"))
    if Datacenter != "" {
        filters = append(filters, filter.Path("networkVlans.primaryRouter.datacenter.name").Eq(Datacenter))
    }
    if Firewall {
        filters = append(filters, filter.Path("networkVlans.dedicatedFirewallFlag").Eq(1))
    }
    objectFilter := filters.Build()
    // fmt.Println("FILTER: ", objectFilter)

    // Sets up the session with authentication headers.
    sess := session.New()
    // uncomment to output API calls as they are made.
    // sess.Debug = true

    // creates a reference to the service object (SoftLayer_Account)
    service := services.GetAccountService(sess)

    // Sets the mask, filter, result limit, and then makes the API call SoftLayer_Account::getHardware()
    vlans, err := service.Mask(objectMask).Filter(objectFilter).
        Offset(resultOffset).Limit(resultLimit).GetNetworkVlans()
    if err != nil {
        return err
    }
    fmt.Printf("Id, VLAN, Name, Datacenter\n")
    for {

        for _, s := range vlans {
            name := "-"
            // The Name property doesn't get returned if the vlan hasn't been named, which will cause a 
            // 'panic: runtime error: invalid memory address' error if we dont check first.
            if s.Name != nil {
                name = *s.Name
            }
            fmt.Printf("%v, %v, %v, %v\n", *s.Id, name, *s.VlanNumber, *s.PrimaryRouter.Datacenter.Name)
        }
        // If we get less than the number of results we asked for, we are at the end of our server list
        if len(vlans) < resultLimit {
            break
        }
        // Increment the offset to get next set of results
        resultOffset = resultOffset + resultLimit
        
        vlans, err = service.Mask(objectMask).Filter(objectFilter).
            Offset(resultOffset).Limit(resultLimit).GetNetworkVlans()
        if err != nil {
            return err
        }
    }

    return nil
}

```


## Details about a specific VLAN

This command shows a quick example of how to print out some important details about a specific vlan. A [VLAN](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan/) object has a lot of fields that could be useful aside from what is shown in this command. Hopefully this example is clear enough to get started though.

>github.com/softlayer/softlayer-go/examples/cmd/vlan_detail.go

```go
package cmd

import (
    "fmt"
    "errors"
    "os"
    "strconv"

    "github.com/spf13/cobra"
    "github.com/jedib0t/go-pretty/v6/table"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
)

func init() {
    rootCmd.AddCommand(detailVlanCmd)
}

var detailVlanCmd = &cobra.Command{
    Use:   "vlan-detail [vlanId]",
    Short: "Vlan Details",
    Long:  `Gets a lot of information about a VLAN`,
    Args: func(cmd *cobra.Command, args []string) error {
        if len(args) < 1 {
            return errors.New("a VLAN ID is required")
        }
        return nil
    },
    RunE: func(cmd *cobra.Command, args []string) error {
        return VlanDetailCommand(cmd, args)
    },
}

func VlanDetailCommand(cmd *cobra.Command, args []string) error {
    // resultLimit := 50
    // resultOffset := 0
    objectMask := `mask[id,name,vlanNumber,primaryRouter[id,hostname,datacenterName,datacenter[name]],
subnets[id,networkIdentifier,note, subnetType]]`

    // Sets up the softlayer-client session and Service
    sess := session.New()
    // sess.Debug = true
    service := services.GetNetworkVlanService(sess)

    // Make sure vlanId is an int
    vlanId, err := strconv.Atoi(args[0])
    if err != nil {
        return err
    }

    // Get the VLAN object from the API https://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject/
    vlan, err := service.Mask(objectMask).Id(vlanId).GetObject()
    if err != nil {
        return err
    }
    
    // https://github.com/jedib0t/go-pretty/tree/main/table
    // A fancy table builder so our output can look nice.
    t := table.NewWriter()
    t.SetOutputMirror(os.Stdout)
    t.AppendHeader(table.Row{"Property", "Value"})

    t.AppendRow([]interface{}{"Id", *vlan.Id})
    t.AppendRow([]interface{}{"Number", *vlan.VlanNumber})
    t.AppendRow([]interface{}{"Name", *vlan.Name})
    t.AppendRow([]interface{}{"Datacenter", *vlan.PrimaryRouter.DatacenterName})
    t.AppendRow([]interface{}{"Primary Router", *vlan.PrimaryRouter.Hostname})

    if len(vlan.Subnets) > 0  {
        subnetTable := table.NewWriter()
        subnetTable.AppendHeader(table.Row{"Id", "Network", "Type", "Note"})
        for _, subnet := range vlan.Subnets {
            note := "-"
            // Subnets do not always have notes, this is required to avoid invalid memory address errors
            if subnet.Note != nil {
                note = *subnet.Note
            }
            subnetTable.AppendRow([]interface{}{*subnet.Id, *subnet.NetworkIdentifier, *subnet.SubnetType, note})
        }
        // Renders the subnet table to the main table instead of main output
        t.AppendRow([]interface{}{"Subnets", subnetTable.Render()})
    }
    // Prints out the table
    t.Render()
    return nil
}
```

## Set a VLANs name

This example displays how to make an API request that requires parameters be sent in. This will edit a VLANs name property to be whatever you input.

>github.com/softlayer/softlayer-go/examples/cmd/vlan_name.go

```go
package cmd

import (
    "fmt"
    "errors"
    "strconv"

    "github.com/spf13/cobra"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/datatypes"
    "github.com/softlayer/softlayer-go/session"
)

func init() {
    vlanNameCmd.Flags().StringVarP(&VlanName, "name", "n", "", "New VLAN name")
    vlanNameCmd.MarkFlagRequired("name")
    rootCmd.AddCommand(vlanNameCmd)
}

var VlanName string
var vlanNameCmd = &cobra.Command{
    Use:   "vlan-name [vlanId]",
    Short: "Set a VLAN's name",
    Long:  `Set a VLAN's name.`,
    Args: func(cmd *cobra.Command, args []string) error {
        if len(args) < 1 {
            return errors.New("a VLAN ID is required")
        }
        return nil
    },
    RunE: func(cmd *cobra.Command, args []string) error {
        return VlanNameCommand(cmd, args)
    },
}

func VlanNameCommand(cmd *cobra.Command, args []string) error {
    // Sets up the softlayer-client session and Service
    sess := session.New()
    // sess.Debug = true
    service := services.GetNetworkVlanService(sess)

    // Make sure vlanId is an int
    vlanId, err := strconv.Atoi(args[0])
    if err != nil {
        return err
    }

    // https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan/
    // only Name and Note are editable on a Vlan object.
    vlanSkel := datatypes.Network_Vlan{
        Name: &VlanName,
    }
    // https://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/editObject/
    _, err = service.Id(vlanId).EditObject(&vlanSkel)
    if err != nil {
        return err
    }
    fmt.Printf("Set name of VLan %v to %v\n", vlanId, VlanName)
    return nil
}
```


## Cancel a Vlan

>github.com/softlayer/softlayer-go/examples/cmd/vlan_cancel.go

```go
package cmd

import (
    "fmt"
    "errors"
    "strconv"

    "github.com/spf13/cobra"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/datatypes"
    "github.com/softlayer/softlayer-go/session"
)

func init() {
    rootCmd.AddCommand(vlanDeleteCmd)
}

var VlanName string
var vlanDeleteCmd = &cobra.Command{
    Use:   "vlan-delete [vlanId]",
    Short: "Delete a vlan",
    Long:  `Cancells a VLAN. Only additional VLANs (the ones you pay for and order individually) can be cancelled this way. VLANs that are provisioned automatically will be cancelled automatically as well.`,
    Args: func(cmd *cobra.Command, args []string) error {
        if len(args) < 1 {
            return errors.New("a VLAN ID is required")
        }
        return nil
    },
    RunE: func(cmd *cobra.Command, args []string) error {
        return VlanDeleteCommand(cmd, args)
    },
}

func VlanDeleteCommand(cmd *cobra.Command, args []string) error {
    // Sets up the softlayer-client session and Service
    sess := session.New()
    // sess.Debug = true
    vlanService := services.GetNetworkVlanService(sess)
    billingService := services.GetBillingItemService(sess)

    // Make sure vlanId is an int
    vlanId, err := strconv.Atoi(args[0])
    if err != nil {
        return err
    }    

    // Limiting the mask to only the ID property helps API calls return faster.
    mask := "id"

    // Get the SoftLayer_Network_Vlan's Billing_Item object id
    billingItem, err := vlanService.Id(vlanId).Mask(mask).GetBillingItem()
    // No billingItem means this vlan isn't billed, so can not be cancelled.
    if err != nil {
        fmt.Printf("Unable to get the billing item of Network Vlan:\n\t%s\n", err)
        return err
    }

    // Cancel the SoftLayer_Billing_Item of Vlan.
    result, err := billingService.Id(*billingItem.Id).CancelService()
    // Usually VLANs can not be cancelled because there exists a subnet or other resource on that VLAN.
    if err != nil {
        fmt.Printf("Unable to cancel Network Vlan:\n\t%s\n", err)
        return err
    }

    fmt.Printf("Successfully cancelled vlan %d\n", vlanId)
    fmt.Println(result)
}
```

## Order a Vlan

>github.com/softlayer/softlayer-go/examples/cmd/vlan_order.go

```go
package cmd

import (
    "encoding/json"
    "fmt"

    "github.com/spf13/cobra"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
    "github.com/softlayer/softlayer-go/datatypes"
    "github.com/softlayer/softlayer-go/sl"

)

func init() {
    orderVlanCmd.Flags().StringVarP(&Location, "datacenter", "d", "", "Datacenter name to order in (like dal13)")
    orderVlanCmd.Flags().StringVarP(&Name, "name", "n", "", "Name of this new vlan")
    orderVlanCmd.Flags().IntVarP(&RouterId, "routerId", "r", 0, "RouterId if you want this vlan in a specific POD in a datacenter")
    rootCmd.AddCommand(orderVlanCmd)
}

var Location string
var Name string
var RouterId int

var orderVlanCmd = &cobra.Command{
    Use:   "vlan-order",
    Short: "Orders a Vlan",
    Long:  `Orders a vlan with 32 static public IP addresses.`,
    RunE: func(cmd *cobra.Command, args []string) error {
        return VlanOrderCommand(cmd, args)
    },
}

func VlanOrderCommand(cmd *cobra.Command, args []string) error {
    // Declare the properties like complexType, location, packageId and quantity for the
    // vlan you wish to order
    quantity           := 1
    packageId          := 0
    sendQuoteEmailFlag := true

    // Build a skeleton SoftLayer_Product_Item_Price objects. To get the list of valid
    // prices for the package use the SoftLayer_Product_Package:getItems method
    itemPrices := []datatypes.Product_Item_Price {
            { Id: sl.Int(2018) },     // Price for the new Public Network Vlan
            { Id: sl.Int(1092) },     // Price for 32 Static Public IP Addresses
    }

    // Create a session
    sess := session.New()

    // Get SoftLayer_Product_Order service
    service := services.GetProductOrderService(sess)

    // Build the Container_Product_Order_Network_Vlan containing the order you wish to place.
    orderTemplate := datatypes.Container_Product_Order_Network_Vlan {
        Container_Product_Order : datatypes.Container_Product_Order {
            Prices         : itemPrices,
            PackageId      : sl.Int(packageId),
            Location       : sl.String(Location),
            Quantity       : sl.Int(quantity),
            SendQuoteEmailFlag : sl.Bool(sendQuoteEmailFlag),
        },
        Name     : sl.String(Name),
    }

    if RouterId > 0 {
        orderTemplate.RouterId = sl.Int(RouterId)
    }

    // Use verifyOrder() method to check for errors. Replace this with placeOrder() when
    // you are ready to order.
    receipt, err := service.VerifyOrder(&orderTemplate)
    if err != nil {
        fmt.Printf("Unable to place order:\n - %s\n", err)
        return err
    }

    // Following helps to print the result in json format.
    jsonFormat, jsonErr := json.MarshalIndent(receipt,"","    ")
    if jsonErr != nil {
        fmt.Println(jsonErr)
        return jsonErr
    }

    fmt.Println(string(jsonFormat))
    return nil
}
```