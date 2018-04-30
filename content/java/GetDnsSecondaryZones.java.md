---
title: "GetDnsSecondaryZones.java"
description: "GetDnsSecondaryZones.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Dns_Secondary"
tags:
    - "dns"
---


```
package api.dns;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.dns.Secondary;

import java.util.List;

/**
 * Retrieve the DNS Secondary Zones associated with the SoftLayer_Account.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSecondaryDomains
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Secondary
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetDnsSecondaryZones {

    public GetDnsSecondaryZones(){

        // Declare username and apiKey
        String username = "set me";
        String apiKey = "set me";

        // 1. Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Account.Service accountService = Account.service(client);

        // 2. Use object mask to get the status
        accountService.withMask().secondaryDomains().status();

        try {
            // Retrieve all DNS Secondary Zones
            List<Secondary> domains = accountService.getObject().getSecondaryDomains();

            // Print the result in a table
            printInTable(domains);
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(List<Secondary> list){
        // Following variables are used to format the table
        String formatA = "| %-8s | %-20s | %-18s | %-18s | %-15s | %-10s |%n";
        String formatB = "+ %-8s + %-20s + %-18s + %-18s + %-15s + %-10s +%n";
        String formatC = "| %-8d | %-20s | %-18s | %-18s | %-15s | %-10s |%n";

        // Table - header
        System.out.format(formatA,"ID", "ZONE", "MASTER NAMESERVER", "TRANSFER INTERNAL",
                "LAST TRANSFER", "STATUS");
        System.out.format(formatB," ", " ", " ", " "," ", " ");

        // Table - body
        for (Secondary dns : list) {
            System.out.format(formatC, dns.getId(), dns.getZoneName(),
                    dns.getMasterIpAddress(), dns.getTransferFrequency() + " Minutes",
                    (dns.getLastUpdate() == null) ? "Never" : dns.getLastUpdate().toString(),
                    dns.getStatus().getName());
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetDnsSecondaryZones();
    }
}

```
