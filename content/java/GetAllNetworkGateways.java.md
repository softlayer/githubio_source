---
title: "GetAllNetworkGateways.java"
description: "GetAllNetworkGateways.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
package api.gateway;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.network.Gateway;

import java.util.List;

/**
 * Retrieve all Network Gateways associated with the SoftLayer_Account.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkGateways
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway
 * https://sldn.softlayer.com/article/object-Masks
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetAllNetworkGateways {

    public GetAllNetworkGateways(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Account.Service accountService = Account.service(client);

        // Use object-masks to get information like ip address and number of vlans
        accountService.withMask().networkGateways().id();
        accountService.withMask().networkGateways().name();
        accountService.withMask().networkGateways().networkSpace();
        accountService.withMask().networkGateways().memberCount();
        accountService.withMask().networkGateways().publicIpAddress().ipAddress();
        accountService.withMask().networkGateways().privateIpAddress().ipAddress();

        try {
            // Retrieve all DNS Forward Zones
            List<Gateway> gateways = accountService.getObject().getNetworkGateways();

            // Print the result in a table
            printInTable(gateways);
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(List<Gateway> list){
        // Following variables are used to format the table
        String formatA = "| %-8s | %-20s | %-20s | %-20s | %-20s |%n";
        String formatB = "+ %-8s + %-20s + %-20s + %-20s + %-20s +%n";
        String formatC = "| %-8d | %-20s | %-20s | %-20s | %-20d |%n";

        // Table - header
        System.out.format(formatA,"ID", "GATEWAY", "PUBLIC IP ADDRESS",
                "PRIVATE IP ADDRESS", "ASSOCIATED VLANS");
        System.out.format(formatB," ", " ", " ", " ", " ");

        // Table - body
        for (Gateway gateway : list) {
            String publicIp = gateway.getPublicIpAddress() == null ?
                    "None" : gateway.getPublicIpAddress().getIpAddress();
            String privateIp = gateway.getPrivateIpAddress() == null ?
                    "None" : gateway.getPrivateIpAddress().getIpAddress();

            System.out.format(formatC, gateway.getId(), gateway.getName(),
                    publicIp, privateIp, gateway.getMemberCount());
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetAllNetworkGateways();
    }
}

```
