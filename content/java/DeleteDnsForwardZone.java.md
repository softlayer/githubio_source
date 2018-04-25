---
title: "DeleteDnsForwardZone.java"
description: "DeleteDnsForwardZone.java"
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
import com.softlayer.api.service.dns.Domain;

/**
 * Delete a DNS Forward Zone associated with the SoftLayer_Account.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/deleteObject
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class DeleteDnsForwardZone {

    public DeleteDnsForwardZone(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of DNS you wish to delete
        Long dnsId = new Long(1615891);

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Domain.Service dnsService = Domain.service(client, dnsId);

        try {
            // Delete the DNS domain
            Boolean deleted = dnsService.deleteObject();

            // Print the result
            System.out.println((deleted) ? "Forward DNS successfully deleted!!"
                                         : "Forward DNS could not be deleted");
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

        new DeleteDnsForwardZone();
    }
}

```
