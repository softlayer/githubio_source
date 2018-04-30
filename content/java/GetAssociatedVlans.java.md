---
title: "GetAssociatedVlans.java"
description: "GetAssociatedVlans.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Network_Gateway"
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---


```
package api.gateway;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.gateway.Vlan;
import com.sun.deploy.util.StringUtils;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Get Associated Vlans of Network Gateway.
 * This example shows how to get the associated vlans of Gateway object by using the method
 * SoftLayer_Network_Gateway::getInsideVlans.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway_Vlan
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
 * https://sldn.softlayer.com/article/object-Masks
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetAssociatedVlans {

    public GetAssociatedVlans(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of gateway you wish get data
        Long gatewayId = new Long(245363);

        // Get Api client and service SoftLayer_Network_Gateway
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Gateway.Service gatewayService = Gateway.service(client, gatewayId);

        // Mask to retrieve necessary data
        gatewayService.withMask().insideVlans().id().bypassFlag();
        gatewayService.withMask().insideVlans().networkVlan().id().vlanNumber()
                .networkSpace().primaryRouter().hostname();

        try {
            // Call the method getInsideVlans.
            List<Vlan> insideVlans = gatewayService.getObject().getInsideVlans();

            // Print the result in a table
            printInTable(insideVlans);

        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(List<Vlan> list){
        // Following variables are used to format the table
        String formatA = "| %-8s | %-30s | %-15s | %-15s |%n";
        String formatB = "+ %-8s + %-30s + %-15s + %-15s +%n";

        // Table - header
        System.out.println("\nASSOCIATED VLANS");
        System.out.println(new String(new char[80]).replace("\0", "="));
        System.out.format(formatA,"ID", "ASSOCIATED VLAN", "NETWORK", "STATUS");
        System.out.format(formatB," ", " ", " ", " ");

        // Table - body
        for(Vlan vlan : list){
            // Build a name using hostname.
            List<String> tmp = Arrays.asList(vlan.getNetworkVlan().getPrimaryRouter()
                    .getHostname().split("\\."));
            Collections.reverse(tmp);
            String name = StringUtils.join(tmp,".") + "." +
                    vlan.getNetworkVlan().getVlanNumber();
            // Use build name if Vlan doesn't have one
            name = (vlan.getNetworkVlan().getName() == null)
                        ? name
                        : vlan.getNetworkVlan().getName();
            String status = vlan.getBypassFlag() ? "Bypassed" : "Routed";

            // Print results like in portal
            System.out.format(formatA, vlan.getNetworkVlan().getId(), name,
                    vlan.getNetworkVlan().getNetworkSpace().toLowerCase(), status);
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetAssociatedVlans();
    }
}

```
