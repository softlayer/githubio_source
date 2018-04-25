---
title: "DnsForwardZoneDetails.java"
description: "DnsForwardZoneDetails.java"
date: "2017-11-23"
classes: 
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

/**
 * This example shows how to retrieve all DNS Fordward data and display them like in
 * portal page.
 * See below for more details.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain
 * https://sldn.softlayer.com/article/object-Masks
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class DnsForwardZoneDetails {

    public DnsForwardZoneDetails(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of DNS domain you wish to get its details.
        Long dnsId = new Long(2058563);

        // Get Api client and service SoftLayer_Dns_Domain
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Domain.Service domainService = Domain.service(client, dnsId);

        // Mask to get Resource Records of Domain
        domainService.withMask().resourceRecords();

        try {
            // Retrieve all DNS Resource Records of domain
            Domain dns = domainService.getObject();

            // To display data like in portal page we will use following method
            printInTable(dns);
        } catch (Exception e) {
            System.out.println("Error : " + e.toString());
        }
    }

    /**
     * This method prints the results in a table
     */
    private void printInTable(Domain dns){
        // Following is to specify the format of table
        String format =  " %-15s %-30s %-15s %-15s %n";
        String formatA = "| %-8s | %-25s | %-15s | %-10s | %-25s |%n";
        String formatB = "+ %-8s + %-25s + %-15s + %-10s + %-25s +%n";
        String formatC = "| %-8d | %-25s | %-15s | %-10d | %-25s |%n";

        // SOA information is in first position of Resource Records list.
        ResourceRecord soa = dns.getResourceRecords().get(0);

        // Print DNS Forward details
        System.out.format(format, "NAME: ", dns.getName(),
                "REFRESH: ", soa.getRefresh().toString());
        System.out.format(format, "SERIAL: ", dns.getSerial(),
                "RETRY: ", soa.getRetry().toString());
        System.out.format(format, "CONTACT: ", soa.getResponsiblePerson(),
                "EXPIRE: ", soa.getExpire().toString());
        System.out.format(format, " ", " ", "MINIMUM: ", soa.getMinimum().toString());

        // Print DNS Records
        System.out.println(" EXISTING RECORDS:");
        System.out.println(new String(new char[100]).replace("\0", "="));

        System.out.format(formatA,"ID", "HOST/SERVICE", "RESOURCE TYPE",
                "TTL", "VALUE/TARGET");

        System.out.format(formatB," ", " ", " ", " ", " ");
        for (ResourceRecord record : dns.getResourceRecords()) {
            // SOA record type is displayed along with the domain data
            if(!record.getType().equals("soa")) {
                System.out.format(formatC, record.getId(), record.getHost(),
                        record.getType(), record.getTtl(), record.getData());
            }
        }
    }

    /**
     * This is the main method which is used to run this class.
     *
     * @param args
     * @return Nothing
     */
    public static void main(String args[]) {

        new DnsForwardZoneDetails();
    }
}

```
