---
title: "GetDnsResourceRecords.java"
description: "GetDnsResourceRecords.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
package api.dns;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.dns.Domain;
import com.softlayer.api.service.dns.domain.ResourceRecord;

import java.util.List;

/**
 * Retrieve the DNS Resource Records associated with the SoftLayer_Dns_Domain.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetDnsResourceRecords {

    public GetDnsResourceRecords(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of DNS domain you wish to get its resource records.
        Long dnsId = new Long(1623914);

        // Get Api client and service SoftLayer_Dns_Domain
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Domain.Service domainService = Domain.service(client, dnsId);

        try {
            // Retrieve all DNS Resource Records of domain
            List<ResourceRecord> records = domainService.getResourceRecords();

            // Print the result in a table
            printInTable(records);
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(List<ResourceRecord> list){
        // Following variables are used to format the table
        String formatA = "| %-8s | %-25s | %-15s | %-10s | %-25s |%n";
        String formatB = "+ %-8s + %-25s + %-15s + %-10s + %-25s +%n";
        String formatC = "| %-8d | %-25s | %-15s | %-10d | %-25s |%n";

        // Table - header
        System.out.format(formatA,"ID", "HOST/SERVICE", "RESOURCE TYPE",
                "TTL", "VALUE/TARGET");

        // Table - body
        System.out.format(formatB," ", " ", " ", " ", " ");
        for (ResourceRecord record : list) {
            System.out.format(formatC, record.getId(), record.getHost(),
                    record.getType(), record.getTtl(), record.getData());
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new GetDnsResourceRecords();
    }
}

```
