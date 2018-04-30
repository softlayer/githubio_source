---
title: "GeTags.java"
description: "GeTags.java"
date: "2018-04-25"
classes: 
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

public class GeTags {

	//
	// Get all the tags in the account.
	// 
	// The script gets all the tags in the account we make a simple
	// call th the getTags() in the SoftLayer_Account API service
	//
	// Manual pages
	// see http://sldn.softlayer.com/reference/services/SoftLayer_Account
	// see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTags
	// license <http://sldn.softlayer.com/article/License>
	// author SoftLayer Technologies, Inc. <sldn@softlayer.com>
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

		// Retrieve the tags in the account.
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(accountService.getTags()));

		} catch (Exception e) {
			System.out.println("Unable to retrieve the tags in the account. "
					+ e.getMessage());
		}

	}

}

```
