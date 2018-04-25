---
title: "GetVirtualGuestItems.java"
description: "GetVirtualGuestItems.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
tags:
    - "billing"
---


```
package api.examples;

import com.google.gson.Gson;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;

public class GetVirtualGuestItems {

	// Retrieve the billing items  for the VSIs in the account.
	//
	// This script makes a single call to the getVirtualGuests() method in the
	// SoftLayer_Account API service and uses a object mask to get the
	// billing items and items for each VSIs in the account.
	//
	// Important manual pages
	// http://sldn.softlayer.com/reference/services/SoftLayer_Account
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item
	//
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";

		// Declare the API client
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Account.Service accountService = Account.service(client);

		// Declaring the object mask to get information about the items
		accountService
				.setMask("mask[id, hostname, domain, datacenter[longName], billingItem[item]]");

		// Retrieve our account's hardware records.
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(accountService.getVirtualGuests()));

		} catch (Exception e) {
			System.out
					.println("Unable to retrieve the VSIs. " + e.getMessage());
		}

	}

}

```
