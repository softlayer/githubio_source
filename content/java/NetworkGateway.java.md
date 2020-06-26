---
title: "Working with Network Gateway"
description: "A few examples on interacting with Network Gateway"
date: "2020-06-26"
classes: 
    - "SoftLayer_Network_Gateway"
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---

Route Vlans

Route the vlans in a gateway device.

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.gateway.Vlan;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class RouteVlans {

    public RouteVlans(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of Network_Gateway you wish associate.
        Long gatewayId = new Long(245363);

        /*
         * The id of Network_Vlan objects you wish to Route. These Vlans must be
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

            // Run unbypassVlans method if vlans are associated to gateway
            if(!associatedVlans.isEmpty()){
                gatewayService.unbypassVlans(associatedVlans);

                // Print the results
                System.out.println("Route Vlan request was successfully executed!");
            } else {
                System.out.println("There are not any associated vlan to Route them.");
            }
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    public static void main(String args[]) {
        new RouteVlans();
    }
}

```

Get Gateway Public Vlan

Retrieve the public VLAN for accessing this gateway.

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.Vlan;

public class GetGatewayPublicVlan {

    public GetGatewayPublicVlan(){

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
            Vlan vlan = gatewayService.getPublicVlan();
            // Print the result
            System.out.println("Vlan Id: " + vlan.getId());
            System.out.println("Vlan Number: " + vlan.getVlanNumber());
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    public static void main(String args[]) {
        new GetGatewayPublicVlan();
    }
}

```

Get Gateway Private Vlan

Retrieve the private VLAN for accessing this gateway.

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.Vlan;

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

    public static void main(String args[]) {
        new GetGatewayPrivateVlan();
    }
}

```

Get Associated Vlans

Get Associated Vlans of Network Gateway.
This example shows how to get the associated vlans of Gateway object by using the method.

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.gateway.Vlan;
import com.sun.deploy.util.StringUtils;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

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

    public static void main(String args[]) {
        new GetAssociatedVlans();
    }
}

```

Disassociate Vlan

Disassociate Vlan and Network Gateway.
On this example, we'll retrieve the SoftLayer_Network_Gateway_Vlan object that
contains the SoftLayer_Network_Vlan object. Next, we will delete the retrieved object
in order to disassociate the SoftLayer_Network_Gateway and SoftLayer_Network_Vlan.

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.gateway.Vlan;

import java.util.List;

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

    public static void main(String args[]) {
        new DisassociateVlan();
    }
}

```

Bypass Vlans

Bypass the vlans in a gateway device.

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.gateway.Vlan;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

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

    public static void main(String args[]) {
        new BypassVlans();
    }
}

```

Associate Vlan

Associate Vlan to Network Gateway.
Use the method SoftLayer_Network_Gateway::getPossibleInsideVlans to get a list of all
vlans that can be associated to the Gateway.
On this example, we'll build a SoftLayer_Network_Gateway_Vlan template object to pass
it to SoftLayer_Network_Gateway_Vlan::createObject and creates the association.

```java
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.gateway.Vlan;

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

    public static void main(String args[]) {
        new AssociateVlan();
    }
}

```
