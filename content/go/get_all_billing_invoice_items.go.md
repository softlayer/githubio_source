---
title: "get_all_billing_invoice_items.go"
description: "get_all_billing_invoice_items.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Invoice_Items"
    - "SoftLayer_Billing_Invoice"
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice_Item"
tags:
    - "billing"
---


```
/*
Retrieve all billing invoice items from account.

This script prints all billing invoice items from account, on this case we'll use a large object
mask in order to retrieve a lot of data. To avoid API errors related to "Time out" or or "size limit",
first we'll get de ID of all SoftLayer_Billing_Invoice objects between two dates, on this case we'll
use the method SoftLayer_Account::getInvoices. After that, through loops we will retrieve all invoice
items, here we'll use the method SoftLayer_Billing_Invoice::getItems and "result limits" to avoid errors.
See below for more information.

Example based on question:
http://stackoverflow.com/questions/43666868/getting-error-internal-error-on-postman-and-getting-error-can-not-deseriali
http://stackoverflow.com/questions/43640651/softlayer-rest-call-giving-multiple-entries-for-invoice-in-json-response-when-ob

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Invoice/getItems
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice_Item
https://sldn.softlayer.com/article/object-Filters
https://sldn.softlayer.com/article/object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
*/
package main

import (
	"fmt"
	"strings"
	"encoding/json"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/services"
)

func main() {
	// SoftLayer API username and key
	username := "set me"
	apikey   := "set me"

	// Create a session
	sess := session.New(username, apikey)

	// Get SoftLayer_Account and SoftLayer_Billing_Invoice services
	accountService := services.GetAccountService(sess)
	invoiceService := services.GetBillingInvoiceService(sess)

	// Object mask to get the ID of all SoftLayer_Billing_Invoice objects
	mask := "id;createDate;typeCode"

	// Object mask to get information about SoftLayer_Billing_Invoice_Items
	itemMask := "id;recurringFee;recurringTaxAmount;oneTimeFee;oneTimeTaxAmount;description;" +
		    "hostName;domainName;hourlyRecurringFee;laborFee;laborTaxAmount;setupFee;" +
		    "setupTaxAmount;category[name];location[longName];billingItem[id;activeFlag;" +
		    "hourlyFlag;allowCancellationFlag;cancellationDate;orderItem[id;order[id;" +
		    "userRecord[id,username]]]]"

	// Filter to get all RECURRING invoices between two dates
	filter := `{"invoices":{
	                  "createDate":{
			       "operation":"betweenDate",
			       "options":[{
			            "name":"startDate",
			            "value":["03/25/2017"]
			       },{
			            "name":"endDate",
			            "value": ["04/24/2017"]
			       }]
			  },
			  "typeCode":{
			       "operation":"RECURRING"
			  }
		    }}`

	// Call method getInvoices() in order to retrieve SoftLayer_Billing_Invoice objects.
	invoices, err := accountService.Filter(filter).Mask(mask).GetInvoices()
	if err != nil {
		fmt.Printf("\n Unable to retrieve invoices:\n - %s\n", err)
		return
	}

	// Following loop is to get and print all items of each retrieved invoice
	for _, invoice := range invoices {

		// Print Id, createDate and typeCode of each invoice
		fmt.Printf("\n\nINVOICE ID: %d\t CREATE DATE: %s\t TYPE CODE: %s\n\n",
			invoice.Id, invoice.CreateDate, *invoice.TypeCode)

		// Some invoices have hundred of items and to avoid limitSize or timeout errors
		// we'll use result limits in order to get items 100 by 100.
		limit := 100
		offset := 0
		hasItems := true

		// Following loop is used to get and print items 100 by 100.
		// 'hasItems' will turn FALSE if there isn't more items, the loop will end and
		// code will continue with next invoice.
		for hasItems {
			// Call SoftLayer_Billing_Invoice::getItems method
			items, err :=  invoiceService.Id(*invoice.Id).Mask(itemMask).Limit(limit).Offset(offset).GetItems()
			if err != nil {
				fmt.Printf("\n Unable to retrieve invoice's items:\n - %s\n", err)
				return
			}

			// Following will print retrieved invoices
			for _, item := range items {
				jsonFormat, jsonErr := json.Marshal(item)
				if jsonErr != nil {
					fmt.Println(jsonErr)
					return
				}
				fmt.Printf("\n%s", string(jsonFormat))
			}

			// hasItems will turn FALSE if invoice doesn't have more items and code will
			// continue with next invoice.
			if len(items) > 0 {
				offset += limit
			} else {
				hasItems = false
			}
		}

		// Print a single separator between invoices
		fmt.Printf("\n\n%s", strings.Repeat("-", 150))
	}
}

```
