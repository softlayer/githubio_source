---
title: "GetDnsForwardZones.java"
description: "GetDnsForwardZones.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
package api.dns;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.dns.Domain;


import java.util.List;

/**
 * Retrieve the DNS Forward Zones associated with the SoftLayer_Account.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDomains
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetDnsForwardZones {

    public GetDnsForwardZones(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Account.Service accountService = Account.service(client);

        // Use object mask to get contact
        accountService.withMask().domains().resourceRecords().responsiblePerson();

        try {
            // Retrieve all DNS Forward Zones
            List<Domain> domains = accountService.getObject().getDomains();

            // Print the result in a table
            printInTable(domains);
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(List<Domain> list){
        // Following variables are used to format the table
        String formatA = "| %-8s | %-30s | %-35s | %-10s |%n";
        String formatB = "+ %-8s + %-30s + %-35s + %-10s +%n";
        String formatC = "| %-8d | %-30s | %-35s | %-10d |%n";

        // Table - header
        System.out.format(formatA," ID ", " DOMAIN ", " CONTACT ", " SERIAL ");
        System.out.format(formatB," ", " ", " ", " ");

        // Table - body
        for (Domain dns : list) {
            System.out.format(formatC, dns.getId(), dns.getName(),
                    dns.getResourceRecords().get(0).getResponsiblePerson(), dns.getSerial());
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetDnsForwardZones();
    }
}

```
