---
title: "DeleteDnsRecord.java"
description: "DeleteDnsRecord.java"
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
import com.softlayer.api.service.dns.domain.ResourceRecord;

/**
 * Delete DNS Resource Record .
 * The SoftLayer_Dns_Domain_ResourceRecord::deleteObject method deletes a domain
 * resource record and this cannot be undone. If you remove a resource record in error
 * you will need to re-create it by creating a new SoftLayer_Dns_Domain_ResourceRecord
 * object. You may not delete SOA, NS, or PTR resource records.
 * See below for more details.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/deleteObject
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class DeleteDnsRecord {

    public DeleteDnsRecord(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        /*
         * The id of domain record you wish to remove.
         * You can get list of domain record id's by using the method
         * SoftLayer_Dns_Domain::getResourceRecords.
         */
        Long recordId = new Long(44584793);

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        ResourceRecord.Service recordService = ResourceRecord.service(client, recordId);

        try {
            // Create the DNS Resource Record
            Boolean deleted  = recordService.deleteObject();

            // Print the result
            System.out.println( deleted ? "DNS Record was successfully deleted!!"
                                        : "DNS Record could not be deleted");
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

        new DeleteDnsRecord();
    }
}

```
