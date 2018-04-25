---
title: "GetGatewayMembers.java"
description: "GetGatewayMembers.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway_Member"
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
package api.gateway;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.network.Gateway;
import com.softlayer.api.service.network.gateway.Member;
import com.softlayer.api.service.software.component.Password;

import java.util.List;

/**
 * Get Network Gateway Members.
 * This example shows how to get Gateway Members by using the method
 * SoftLayer_Network_Gateway::getMembers.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getMembers
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway_Member
 * https://sldn.softlayer.com/article/object-Masks
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetGatewayMembers {

    public GetGatewayMembers(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of gateway you wish to get data
        Long gatewayId = new Long(172123);

        // Get Api client and service SoftLayer_Network_Gateway
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Gateway.Service gatewayService = Gateway.service(client, gatewayId);

        // Mask to retrieve necessary data of gateway members
        gatewayService.withMask().members().id().priority();
        gatewayService.withMask().members().hardware().id().fullyQualifiedDomainName().id()
                .primaryIpAddress().primaryBackendIpAddress();
        gatewayService.withMask().members().hardware().operatingSystem().id().passwords()
                .username().password();

        try {
            // Call the method getMembers.
            List<Member> members = gatewayService.getObject().getMembers();

            // Print the result in a table
            printInTable(members);

        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(List<Member> list){
        // Following variables are used to format the table
        String formatA = "| %-8s | %-30s | %-15s | %-15s | %-10s | %-18s |%n";
        String formatB = "+ %-8s + %-30s + %-15s + %-15s + %-10s + %-18s +%n";

        // Table - header
        System.out.println("\nMEMBERS");
        System.out.println(new String(new char[115]).replace("\0", "="));
        System.out.format(formatA,"ID", "MEMBER", "PUBLIC IP", "PRIVATE IP", "PRIORITY",
                "USERNAME/PASSWORD");
        System.out.format(formatB," ", " ", " ", " ", " ", " ", " ");

        // Table - body
        for(Member member : list){
            List<Password> passwords = member.getHardware().getOperatingSystem().getPasswords();
            System.out.format(formatA, member.getId().toString(),
                    member.getHardware().getFullyQualifiedDomainName(),
                    member.getHardware().getPrimaryIpAddress(),
                    member.getHardware().getPrimaryBackendIpAddress(),
                    member.getPriority().toString(),
                    passwords.get(0).getUsername() + "/" + passwords.get(0).getPassword());
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetGatewayMembers();
    }
}

```
