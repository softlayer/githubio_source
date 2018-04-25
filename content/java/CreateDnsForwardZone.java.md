---
title: "CreateDnsForwardZone.java"
description: "CreateDnsForwardZone.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Account"
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
 * Create DNS Forward Zone.
 * The SoftLayer_Dns_Domain::createObject method creates a new Dns Forward Zone.
 * See below for more details.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/createObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class CreateDnsForwardZone {

    public CreateDnsForwardZone(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // Domain name you wish to register
        String domainName = "javaexample.com";
        // The Ip Address of dns
        String ipAddress = "192.168.5.15";

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Domain.Service dnsService = Domain.service(client);

        /*
         * The SoftLayer_Dns_Domain object must have at least one A or AAAA resource
         * record. On this case we need to build a SoftLayer_Dns_Domain_ResourceRecord
         * object.
         * If your domain doesn't contain NS resource records for ns1.softlayer.com
         * or ns2.softlayer.com then createObject will create them for you
         */
        ResourceRecord record = new ResourceRecord();
        record.setData(ipAddress);
        record.setHost("@");
        record.setType("a");

        // Build the templateObject which is a SoftLayer_Dns_Domain
        Domain dns = new Domain();
        dns.setName(domainName);
        dns.getResourceRecords().add(record);

        try {
            // Create the DNS Fordward Zone
            Domain domain = dnsService.createObject(dns);

            // Print the result
            System.out.println("Domain id: " + domain.getId());
            System.out.println("Domain name: " + domain.getName());
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

        new CreateDnsForwardZone();
    }
}

```
