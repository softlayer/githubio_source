---
title: "GetBillingInfo.java"
description: "GetBillingInfo.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Billing_Info"
    - "SoftLayer_Account"
tags:
    - "billing"
---


```
package api.examples;

import com.google.gson.Gson;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;

public class GetBillingInfo {

	// Retrieve the billing info for the Bare Metals in the account.
	//
	// This script makes a single call to the getHardware() method in the
	// SoftLayer_Account API service and uses a object mask to get the
	// billing info for each Bare Metal server in the account.
	//
	// Important manual pages
	// http://sldn.softlayer.com/reference/services/SoftLayer_Account
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Info
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
				.setMask("mask[id, hostname, domain, datacenter[longName], billingItem[recurringFee]]");

		// Retrieve the bare metal servers for the account.
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(accountService.getHardware()));

		} catch (Exception e) {
			System.out.println("Unable to retrieve the Bare Metal list. "
					+ e.getMessage());
		}

	}

}

```
