---
title: "AssociateVlan.java"
description: "AssociateVlan.java"
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
import com.softlayer.api.service.network.gateway.Vlan;

/**
 * Associate Vlan to Network Gateway.
 * Use the method SoftLayer_Network_Gateway::getPossibleInsideVlans to get a list of all
 * vlans that can be associated to the Gateway.
 * On this example, we'll build a SoftLayer_Network_Gateway_Vlan template object to pass
 * it to SoftLayer_Network_Gateway_Vlan::createObject and creates the association.
 * See below for more details:
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getPossibleInsideVlans
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/createObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway_Vlan
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class AssociateVlan {

    public AssociateVlan(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of Network_Gateway you wish associate.
        Long gatewayId = new Long(245363);

        /*
         * The id of Network_Vlan you wish associate. You can get available Vlans by
         * executing the SoftLayer_Network_Gateway::getPossibleInsideVlans method.
         */
        Long vlanId = new Long(1455755);

        // Get Api client and service Get SoftLayer_Network_Gateway_Vlan
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Vlan.Service gatewayVlanService = Vlan.service(client);

        // Build the template object that will be used to associate objects.
        Vlan templateObject = new Vlan();
        templateObject.setNetworkGatewayId(gatewayId);
        templateObject.setNetworkVlanId(vlanId);

        try {
            // Create the association by running the createObject method.
            Vlan vlanAssociated = gatewayVlanService.createObject(templateObject);

            // Print the results
            System.out.println("Gateway and Vlan were successfully associated: " +
                    vlanAssociated.getId());
            System.out.println("Gateway id: " + gatewayId);
            System.out.println("Vlan id: " + vlanId);
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

        new AssociateVlan();
    }
}

```
