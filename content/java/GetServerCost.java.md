---
title: "GetServerCost.java"
description: "GetServerCost.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "billing"
---


```
package api.examples;

import com.google.gson.Gson;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;

// Get the recurring cost of a single server or all servers on your account.
// 
// Get a list of servers on a SoftLayer account along with their recurring
// monthly costs. We can get that by calling getHardware() in the
// SoftLayer_Account API service with an object mask to retrieve cost.
//
// Manual pages
// see http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
// see http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getCost
// license <http://sldn.softlayer.com/article/License>
// author SoftLayer Technologies, Inc. <sldn@softlayer.com>
// 
public class GetServerCost {
    
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";
		        
		// Declare the API client
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Account.Service accountService = Account.service(client);
	    
		// Add the object mask to the call.
		accountService.setMask("mask(SoftLayer_Hardware_Server).cost");

		// Retrieve our account's hardware records.
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(accountService.getHardware()));

		} catch (Exception e) {
			System.out.println("Unable to retrieve the Bare Metal list. " + e.getMessage());
		}
	}

}

```
