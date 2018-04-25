---
title: "GetSubnets.java"
description: "GetSubnets.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Network_Subnet"
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

public class GetSubnets {
 
	// Retrieve the subnets for a VLAN 
	//
	// Retrieve all the subnets for a determinate VLAN
	// associated with a SoftLayer customer account 
	// We do this with a call to the getSubnets() method in the 
	// SoftLayer_Network_Vlan API service. See below for more details.
	//
	// Important manual pages:
	// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
	// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets
	//
	// License: http://sldn.softlayer.com/article/License
	// Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";

		// the VLAN id you wish to see its subnets
		Long vlanId = new Long(557984);

		// Declare the API client
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Vlan.Service vlanService = Vlan.service(client, vlanId);

		// Send the request to get the subnets
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(vlanService.getSubnets()));

		} catch (Exception e) {
			System.out.println("Unable to retrieve the subnets. "
					+ e.getMessage());
		}
	}
}

```
