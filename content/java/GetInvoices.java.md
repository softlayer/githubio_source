---
title: "GetInvoices.java"
description: "GetInvoices.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Invoice"
tags:
    - "billing"
---


```
package api.examples;

import com.google.gson.Gson;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;

public class GetInvoices {

	// Retrieve the invoice information.
	//
	// This script makes a single call to the getInvoices() method in the
	// SoftLayer_Account API service and uses a object mask to get more
	// information about the invoices.
	//
	// Important manual pages
	// http://sldn.softlayer.com/reference/services/SoftLayer_Account
	// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
	// 
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";

		// Declare the API client.
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Account.Service accountService = Account.service(client);

		// Declaring the object mask to get information about the billing item.
		accountService
				.setMask("mask[payment,amount,invoiceTotalOneTimeAmount,invoiceTotalRecurringAmount,invoiceTotalOneTimeTaxAmount,invoiceTotalRecurringTaxAmount]");

		// Retrieve the invoices for the account.
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(accountService.getInvoices()));

		} catch (Exception e) {
			System.out
					.println("Unable to retrieve the Invoices. " + e.getMessage());
		}

	}

}

```
