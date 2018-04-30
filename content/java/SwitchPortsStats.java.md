---
title: "SwitchPortsStats.java"
description: "SwitchPortsStats.java"
date: "2018-04-25"
classes: 
    - "SoftLayer_Container_Network_Port_Statistic"
    - "SoftLayer_NetworkComponent"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Component"
tags:
    - "vlans"
---


```
package api.examples;

import com.google.gson.Gson;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Hardware;
import com.softlayer.api.service.network.Component;

public class SwitchPortsStats {

	// Retrieve a list of switchport statistics for a server's network interfaces.
	//
	// This script makes a single call to the getPortStatistics() method in the
	// SoftLayer_Network_Component API service
	// (http://sldn.softlayer.com/reference/services/SoftLayer_NetworkComponent/getPortStatistics)
	// for each of a server's network components to query port statistics for that
	// interface from SoftLayer's switches. Port statistics are modeled by the
	// SoftLayer__Container_Network_Port_Statistic data type
	// (http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_Port_Statistic).
	// See below for more details.
	//
	public static void main(String[] args) {
		// Your SoftLayer API username and key.
		// Generate one at
		// https://manage.softlayer.com/Administrative/apiKeychain
		String user = "";
		String apikey = "apikey_goes_here";

		// Your server's id. Call the getHardware() method in the
		// SoftLayer_Account API
		// service
		// (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
		// to get a list of your account's hardware records.
		Long serverId = new Long(87165);

		// Declare the API client
		ApiClient client = new RestApiClient().withCredentials(user, apikey);
		Hardware.Service hardwareService = Hardware.service(client, serverId);

		// Switchport statistics are measured off the server's network components. Use
		// an object mask to network component records along with our server record.
		hardwareService.setMask("mask[networkComponents]");

		try {
			// Make the call to retrieve our hardware record. Once we have that we can query
			// the server's network components.
			Gson gson = new Gson();
			Hardware server = hardwareService.getObject();

			// Loop through our server's network components. For each NIC make a call to the
			// SoftLayer_Network_Component API service method getPortStatics() to get a list
			// of switchport statistics retrieved from the switch on the other side of your
			// NIC. Print a simple report per NIC.
			for (Component component : server.getNetworkComponents()) {
				System.out.println(component.getId());
				Component.Service componentService = Component.service(client,
						component.getId());
				System.out.println(gson.toJson(componentService
						.getPortStatistics()));
			}

		} catch (Exception e) {
			System.out.println("Unable to retrieve switchport statics for. "
					+ e.getMessage());
		}

	}

}

```
