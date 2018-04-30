---
title: "CreateDnsRecord.java"
description: "CreateDnsRecord.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Account"
tags:
    - "dns"
---


```
package api.dns;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.dns.domain.ResourceRecord;

/**
 * Create DNS Resource Record .
 * The SoftLayer_Dns_Domain_ResourceRecord::createObject method creates a new domain
 * resource record.
 * See below for more details.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/createObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class CreateDnsRecord {

    public CreateDnsRecord(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of DNS domain you wish to add a new record
        Long dnsId = new Long(1623914);

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        ResourceRecord.Service recordService = ResourceRecord.service(client);

        /*
         * Build the resource record taking account the following
         *  - Record requires the associated domainId.
         *  - Each resource record contains a host and data property.
         *  - Type can take one of the following values:
         *      "a"     - for address records
         *      "aaaa"  - for address records
         *      "cname" - for canonical name records
         *      "mx"    - for mail exchanger records
         *      "ns"    - for name server records
         *      "ptr"   - for pointer records in reverse domains
         *      "soa"   - for a domain's start of authority record
         *      "spf"   - for sender policy framework records
         *      "srv"   - for service records
         *      "txt"   - for text records
         */
        ResourceRecord template = new ResourceRecord();
        template.setDomainId(dnsId);
        template.setData("197.168.2.10");
        template.setHost("javamail.com");
        template.setType("mx");
        template.setTtl(new Long(1800));

        try {
            // Create the DNS Resource Record
            ResourceRecord record  = recordService.createObject(template);

            // Print the result
            System.out.println("ID: " + record.getId());
            System.out.println("Host: " + record.getHost());
            System.out.println("Type: " + record.getType());
            System.out.println("Data: " + record.getData());
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

        new CreateDnsRecord();
    }
}

```
