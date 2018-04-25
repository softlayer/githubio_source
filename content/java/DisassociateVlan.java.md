---
title: "DisassociateVlan.java"
description: "DisassociateVlan.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
    - "SoftLayer_Network_Vlan"
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

import java.util.List;

/**
 * Disassociate Vlan and Network Gateway.
 * On this example, we'll retrieve the SoftLayer_Network_Gateway_Vlan object that
 * contains the SoftLayer_Network_Vlan object. Next, we will delete the retrieved object
 * in order to disassociate the SoftLayer_Network_Gateway and SoftLayer_Network_Vlan.
 * See below for more details:
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/deleteObject
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class DisassociateVlan {

    public DisassociateVlan(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of gateway you wish disassociate a vlan.
        Long gatewayId = new Long(245363);

        // The id of Network_Vlan you wish disassociate.
        Long vlanId = new Long(1455755);

        // Get Api client and service SoftLayer_Network_Gateway
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Gateway.Service gatewayService = Gateway.service(client, gatewayId);

        try {
            // Retrieve SoftLayer_Network_Gateway_Vlan objects
            List<Vlan> associatedVlans = gatewayService.getInsideVlans();

            // Retrieve SoftLayer_Network_Gateway_Vlan that contains the Network_Vlan
            Vlan gatewayVlan = associatedVlans.stream()
                    .filter(vlan -> vlan.getNetworkVlanId().equals(vlanId))
                    .findFirst()
                    .orElse(null);

            if(gatewayVlan != null){
                // Get SoftLayer_Network_Gateway_Vlan service
                Vlan.Service gatewayVlanService = Vlan.service(client, gatewayVlan.getId());

                // Delete the Network_Gateway_Vlan object in order to disassociate the
                // Network_Vlan and Network_Gateway.
                gatewayVlanService.deleteObject();

                // Print the results
                System.out.println("Association between following objects was removed");
                System.out.println("Gateway id: " + gatewayId);
                System.out.println("Vlan id: " + vlanId);
            } else {
                System.out.println("The Network_Vlan " + vlanId +
                        " is nos associated to Network_Gateway " + gatewayId);
            }
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

        new DisassociateVlan();
    }
}

```
