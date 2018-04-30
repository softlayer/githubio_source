---
title: "GetDetailsVlan.java"
description: "GetDetailsVlan.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Subnet_IpAddress"
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

public class GetDetailsVlan {
 
	// Retrieve account VLAN and subnet information.
	//
	// Retrieve a list of all VLANs associated with a SoftLayer customer account 
	// and print a simple report detailing these VLANs and the subnets assigned to 
	// them. We do this with a call to the getNetworkVlans() method in the 
	// SoftLayer_Account API service using an object mask to retrieve the VLANs' 
	// associated subnets and primary router records. See below for more details.
	//
	// Important manual pages:
	// http://sldn.softlayer.com/reference/services/SoftLayer_Account
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
	// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
	// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans
	//
	// License: http://sldn.softlayer.com/article/License
	// Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";
		
		// the VLAN id you wish to see its details
		Long vlanId = new Long(557984);

		// Declare the API client
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Vlan.Service vlanService = Vlan.service(client, vlanId);
        
		// declaring an object mask to get more information about the VLANs
		// such as the primaryRouter and the subnets
		vlanService.setMask("mask[primaryRouter, subnets[ipAddresses]]");

		// Send the request to get the VLAN and print the result
		try {
			Gson gson = new Gson();
			System.out.println(gson.toJson(vlanService.getObject()));

		} catch (Exception e) {
			System.out.println("Unable to retrieve the VLAN. "
					+ e.getMessage());
		}

	}

}

```
