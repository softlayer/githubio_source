---
title: "CancelVlan.java"
description: "CancelVlan.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
package api.examples;

import com.google.gson.Gson;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Vlan;
import com.softlayer.api.service.billing.Item;

public class CancelVlan {
	// Example to cancel a VLAN
	// The script will get the Billing_Item id of the VLAN service
	// then it will cancel the VLAN service
	// reference pages
	// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
	// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
	// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item
	// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";

		// the VLAN id you wish to cancel
		Long vlanId = new Long(557984);

		// Declare the API client
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Vlan.Service vlanService = Vlan.service(client, vlanId);

		vlanService.setMask("mask[billingItem]");

		// Send the request to get the subnets
		try {
			Gson gson = new Gson();
			Vlan vlan = vlanService.getObject();
			Item.Service itemService = Item.service(client, vlan
					.getBillingItem().getId());
			itemService.cancelService();

		} catch (Exception e) {
			System.out.println("Unable to cancel service. " + e.getMessage());
		}

	}

}


```
