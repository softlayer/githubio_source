---
title: "EditDnsSecondaryZone.java"
description: "EditDnsSecondaryZone.java"
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
 * Edit DNS Secondary Zone.
 * This example shows how to edit a DNS Secondary zone. On this case we will build a
 * SoftLayer_Dns_Secondary object template to pass it to editObject method.
 * See details below.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/editObject
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class EditDnsSecondaryZone {

    public EditDnsSecondaryZone(){

        // Declare username and apiKey
        String username = "set-me";
        String apiKey = "set-me";

        // The id of Secondary DNS Zone you wish to edit
        Long dnsId = new Long(21537);

        // Get Api client and service SoftLayer_Account
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Secondary.Service dnsService = Secondary.service(client, dnsId);

        /*
         * Build the SoftLayer_Dns_Secondary object template.
         * You may only edit the masterIpAddress and transferFrequency properties of
         * secondary DNS record. ZoneName may not be altered after a secondary DNS record
         * has been created.
         */
        Secondary templateObject = new Secondary();
        templateObject.setMasterIpAddress("122.22.22.0");
        templateObject.setTransferFrequency(new Long(5));

        try {
            // Edit the DNS Secondary Zone
            Boolean edited = dnsService.editObject(templateObject);

            // Print the result
            System.out.println(edited ? "DNS Zone has been edited successfully!!"
                                      : "DNS Zone could not be edited.");
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

        new EditDnsSecondaryZone();
    }
}

```
