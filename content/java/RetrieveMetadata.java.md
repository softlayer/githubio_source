---
title: "RetrieveMetadata.java"
description: "RetrieveMetadata.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
    - "metadata"
---


```
package api.examples;

import com.google.gson.Gson;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;

public class RetrieveMetadata {

	/**
	 * Retrieves the user data for the VSIs in the account
	 * 
	 * The script gets the user metadata for a VSI in the account we make a simple
	 * call the the getVirtualGuests() in the SoftLayer_Virtual_Guest API service
	 * and we set an object mask to get the information about the user data
	 * 
	 * Manual pages
	 * see http://sldn.softlayer.com/reference/services/SoftLayer_Account
	 * see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
	 * license <http://sldn.softlayer.com/article/License>
	 * author SoftLayer Technologies, Inc. <sldn@softlayer.com>
	 */
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";

		// Declare the API client.
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Account.Service accountService = Account.service(client);

		// # Add the object mask to the call to get the information about the user data.
		accountService.setMask("mask[userData]");

		// Retrieve our account's VSIs records.
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(accountService.getVirtualGuests()));

		} catch (Exception e) {
			System.out.println("Unable to retrieve the metadata information. "
					+ e.getMessage());
		}

	}

}

```
