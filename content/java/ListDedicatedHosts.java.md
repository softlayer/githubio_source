---
title: "ListDedicatedHosts.java"
description: "ListDedicatedHosts.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhost"
---


```
package DedicatedHost;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Account;
import com.softlayer.api.service.virtual.DedicatedHost;

import java.util.List;

/**
 * Get all Dedicated Hosts in the Account.
 *
 * This example shows how to get a list of SoftLayer_Virtual_DedicatedHost objects by using the method
 * SoftLayer_Account::getDedicatedHosts.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDedicatedHosts
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class ListDedicatedHosts {

    public static void main(String args[]) {
        // Your SoftLayer username and api key
        String username = "set me";
        String apiKey = "set me";

        // Get Api Client and service
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        Account.Service accountService = Account.service(client);

        try{
            // Call to getDedicatedHosts method ti obtain a list of SoftLayer_Virtual_DedicatedHost
            List<DedicatedHost> dedicatedHostList = accountService.getDedicatedHosts();

            // Print response in JSON format
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(dedicatedHostList));
        } catch (Exception e)
        {
            System.out.println("Unable to list the dedicated hosts: " + e);
        }
    }
}

```
