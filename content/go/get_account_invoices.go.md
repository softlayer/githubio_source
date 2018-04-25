---
title: "get_account_invoices.go"
description: "get_account_invoices.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "billing"
---


```
/*
Retrieve information of invoices in the account.

This script makes a single call to the getInvoices() method in the SoftLayer_Account API service
and uses a object masks to get the specific information of each invoice.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
	"strings"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account service
	service := services.GetAccountService(sess)

	// Declare object mask used to get information about invoices
	mask := "id;payment;amount;invoiceTotalOneTimeAmount;invoiceTotalRecurringAmount;" +
		"invoiceTotalOneTimeTaxAmount;invoiceTotalRecurringTaxAmount"

	// Call method getInvoices() in order to retrieve SoftLayer_Billing_Invoice objects.
	invoices, err := service.Mask(mask).GetInvoices()
	if err != nil {
		fmt.Printf("\n Unable to retrieve invoices:\n - %s\n", err)
		return
	}

	// Following helps to print the result en JSON format.
	for _, invoice := range invoices {
		jsonFormat, jsonErr := json.MarshalIndent(invoice, "", "     ")
		if jsonErr != nil {
			fmt.Println(jsonErr)
			return
		}
		fmt.Printf("\n%s", string(jsonFormat))
		// Single separator
		fmt.Printf("\n%s", strings.Repeat("-", 120))
	}
}

```
