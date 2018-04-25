---
title: "BypassVlans.java"
description: "BypassVlans.java"
date: "2017-11-23"
classes: 
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

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Bypass the vlans in a gateway device.
 *
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/bypassVlans
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class BypassVlans {

    public BypassVlans(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of Network_Gateway you wish associate.
        Long gatewayId = new Long(245363);

        /*
         * The id of Network_Vlan objects you wish to Bypass. These Vlans must be
         * associated to the Network_Gateway.
         */
        List<Long> vlanIds = new ArrayList<Long>(){{
            add(new Long(1455745));
            add(new Long(1071043));
        }};

        // Get Api client and service SoftLayer_Network_Gateway
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Gateway.Service gatewayService = Gateway.service(client, gatewayId);

        try {
            // Retrieve SoftLayer_Network_Gateway_Vlan objects
            List<Vlan> associatedVlans = gatewayService.getInsideVlans().stream()
                    .filter(vlan -> vlanIds.contains(vlan.getNetworkVlanId()))
                    .collect(Collectors.toList());

            // Run bypassVlans method if vlans are associated to gateway
            if(!associatedVlans.isEmpty()){
                gatewayService.bypassVlans(associatedVlans);

                // Print the results
                System.out.println("Bypass Vlan request was successfully executed!");
            } else {
                System.out.println("There are not any associated vlan to Bypass them.");
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

        new BypassVlans();
    }
}

```
