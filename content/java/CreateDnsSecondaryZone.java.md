---
title: "CreateDnsSecondaryZone.java"
description: "CreateDnsSecondaryZone.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Dns_Secondary"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
package api.dns;

import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.dns.Secondary;

/**
 * Create DNS Secondary Zone.
 * The SoftLayer_Dns_Secondary::createObject method creates a new Dns Secondary Zone.
 * See below for more details.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Secondary/createObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Secondary
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class CreateDnsSecondaryZone {

    public CreateDnsSecondaryZone(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // Domain name you wish to register
        String domainName = "javaexample.com";
        // The Ip Address of dns
        String ipAddress = "192.168.5.17";
        // How often a secondary DNS zone should be transferred in minutes
        Long frequency = new Long(10);

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Secondary.Service dnsService = Secondary.service(client);

        // Build the templateObject which is a SoftLayer_Dns_Domain
        Secondary dns = new Secondary();
        dns.setZoneName(domainName);
        dns.setMasterIpAddress(ipAddress);
        dns.setTransferFrequency(frequency);

        try {
            // Create the DNS Fordward Zone
            Secondary domain = dnsService.createObject(dns);

            // Print the result
            System.out.println("Domain id: " + domain.getId());
            System.out.println("Domain name: " + domain.getZoneName());
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

        new CreateDnsSecondaryZone();
    }
}

```
