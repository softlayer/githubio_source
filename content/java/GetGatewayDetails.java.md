---
title: "GetGatewayDetails.java"
description: "GetGatewayDetails.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
package api.gateway;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;

/**
 * Get Network Gateway details.
 * This example shows how to get the Gateway object and print its information like
 * in Portal.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway
 * https://sldn.softlayer.com/article/object-Masks
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetGatewayDetails {

    public GetGatewayDetails(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of gateway you wish to edit
        Long gatewayId = new Long(172123);

        // Get Api client and service SoftLayer_Network_Gateway
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Gateway.Service gatewayService = Gateway.service(client, gatewayId);

        // Mask for Gateway object
        gatewayService.withMask().id().name().networkSpace().groupNumber().memberCount();
        gatewayService.withMask().status().name();
        gatewayService.withMask().publicIpAddress().ipAddress();
        gatewayService.withMask().privateIpAddress().ipAddress();
        gatewayService.withMask().publicIpv6Address().ipAddress();

        try {
            // Call the method getObject.
            Gateway gateway = gatewayService.getObject();

            // Print the result in a table
            printInTable(gateway);

        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(Gateway gateway){
        // Following variable is used to format the table
        String format  = " %-20s  %-15s  %-20s  %-15s  %-20s  %-15s %n";

        // Print Gateway details
        System.out.println("\nGATEWAY: '" + gateway.getName() + "'");
        System.out.println(new String(new char[130]).replace("\0", "-"));

        System.out.format(format, "NETWORK: ",
                gateway.getNetworkSpace().equals("BOTH") ? "public/private"
                                                         : gateway.getNetworkSpace().toLowerCase(),
                "STATUS: ", gateway.getStatus().getName().toLowerCase(),
                "GROUP NUMBER: ", gateway.getGroupNumber().toString());
        System.out.format(format, "PUBLIC GATEWAY IP: ",
                gateway.getPublicIpAddress().getIpAddress() , "PRIVATE GATEWAY IP: ",
                gateway.getPrivateIpAddress().getIpAddress(), "PUBLIC GATEWAY IPv6: ",
                gateway.getPublicIpv6Address().getIpAddress());
        System.out.format(format, "CONFIGURATION: ", gateway.getMemberCount() > 1 ?
                "high availability" : "standalone",
                " ", " ", " "," ");
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetGatewayDetails();
    }
}

```
