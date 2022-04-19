---
title: "Working with Virtual Guests"
description: "A collection of CLI Examples on how to interact with Virtual Guests."
date: "2022-04-14"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "virtualguest"
    - "virtualguests"
    - "createobject"
    - "upgradevirtualguest"
---

Read up on the [Golang Example Framework](/go/exampleFramework) for information on how to setup the CLI Framework to get this code to run easily.


## Creating a Virtual Guest

These scripts make a paginated API call to [SoftLayer_Virtual_Guest::createObject()](/reference/services/SoftLayer_Virtual_Guest/createObject/) and print the id and the hostname of the new instance.

The first script calls the method from the `main` function

```go
package main

import (
	"fmt"
	"log"

	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

// A virtual guest template
//
// (use convenience functions to get pointers from literals, as needed)
var vGuestTemplate = datatypes.Virtual_Guest{
	Hostname:                     sl.String("sample"),
	Domain:                       sl.String("example.com"),
	MaxMemory:                    sl.Int(4096),
	StartCpus:                    sl.Int(1),
	Datacenter:                   &datatypes.Location{Name: sl.String("wdc01")},
	OperatingSystemReferenceCode: sl.String("UBUNTU_LATEST"),
	LocalDiskFlag:                sl.Bool(true),
}

func main() {
	// Create a session
	sess := session.New()

	service := services.GetVirtualGuestService(sess)

	// Create the virtual guest from the template
	//
	// We also specify an (optional) object mask, to read back some values
	vGuest, err := service.Mask("id,hostname,domain").CreateObject(&vGuestTemplate)
	if err != nil {
		log.Fatal(err)
	} else {
		fmt.Printf(
		"\nNew Virtual Guest with ID %d being provisioned\n", *vGuest.Id)
	}
}

```

The second script calls the method from the `doCreateVMTest` function

```go
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	sess := session.New()
	doCreateVMTest(sess)
}


func doCreateVMTest(sess *session.Session) {
	service := services.GetVirtualGuestService(sess)

	// Create a Virtual_Guest instance as a template
	vGuestTemplate := datatypes.Virtual_Guest{}

	//Set Creation values - use helpers from the sl package to set pointer values
	vGuestTemplate.Hostname = sl.String("sample")
	vGuestTemplate.Domain = sl.String("example.com")
	vGuestTemplate.MaxMemory = sl.Int(4096)
	vGuestTemplate.StartCpus = sl.Int(1)
	vGuestTemplate.Datacenter = &datatypes.Location{Name: sl.String("wdc01")}
	vGuestTemplate.OperatingSystemReferenceCode = sl.String("UBUNTU_LATEST")
	vGuestTemplate.LocalDiskFlag = sl.Bool(true)

	vGuest, err := service.Mask("id;domain").CreateObject(&vGuestTemplate)
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	} else {
		fmt.Printf("\nNew Virtual Guest created with ID %d\n", *vGuest.Id)
		fmt.Printf("Domain: %s\n", *vGuest.Domain)
	}
}

```

## Listing Virtual Guests

This script makes a paginated API call to [SoftLayer_Account::getVirtualGuests()](/reference/services/SoftLayer_Account/getVirtualGuests/) and prints ids, hostnames and domains of ten account’s associated virtual guest objects.

```go
package main

import (
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	sess := session.New()
	doListAccountVMsTest(sess)
}

func doListAccountVMsTest(sess *session.Session) {
	// Get the Account service
	service := services.GetAccountService(sess)

	// List VMs
	vms, err := service.Mask("id;hostname;domain").Limit(10).GetVirtualGuests()
	if err != nil {
		fmt.Printf("Error retrieving Virtual Guests from Account: %s\n", err)
		return
	} else {
		fmt.Println("VMs under Account:")
	}

	for _, vm := range vms {
		fmt.Printf("\t[%d]%s.%s\n", *vm.Id, *vm.Hostname, *vm.Domain)
	}
}

```

## Canceling a Virtual Guest

This script makes a paginated API call to [SoftLayer_Virtual_Guest::deleteObject](/reference/services/SoftLayer_Virtual_Guest/deleteObject/).

```go
package main

package main

import (
	"fmt"
	"log"

	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

var guestId = 24438563

func main() {
	// Create a session
	sess := session.New()

	// Get the virtual guest service
	service := services.GetVirtualGuestService(sess)

	// Set the object ID and delete the guest
	success, err := service.Id(guestId).DeleteObject()

	if err != nil {
		log.Fatal(err)
	} else if success == false {
		log.Fatal("Error deleting virtual guest")
	} else {
		fmt.Println("Virtual Guest deleted successfully")
	}
}

```


## Upgrading a Virtual Guest

This example demonstrates the use of helper functions that simplify the process of placing a virtual guest upgrade order

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
