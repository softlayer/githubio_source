---
title: "GetGatewayPrivateVlan.java"
description: "GetGatewayPrivateVlan.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
package api.gateway;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.Vlan;


/**
 * Get Private Vlan of a Network Gateway.
 * This example shows how to get the private vlan of a Gateway.
 * At the moment cannot get local or relational properties of a private Vlan by using
 * object-mask feature.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getPrivateVlan
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetGatewayPrivateVlan {

    public GetGatewayPrivateVlan(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of gateway you wish to edit
        Long gatewayId = new Long(172123);

        // Get Api client and service SoftLayer_Network_Gateway
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Gateway.Service gatewayService = Gateway.service(client, gatewayId);

        try {
            // Call the method getPublicVlan
            Vlan vlan = gatewayService.getPrivateVlan();
            // Print the result
            System.out.println("Vlan Id: " + vlan.getId());
            System.out.println("Vlan Number: " + vlan.getVlanNumber());
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetGatewayPrivateVlan();
    }
}

```
