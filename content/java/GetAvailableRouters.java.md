---
title: "GetAvailableRouters.java"
description: "GetAvailableRouters.java"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
    - "SoftLayer_Location"
tags:
    - "dedicatedhost"
---


```
package DedicatedHost;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.Hardware;
import com.softlayer.api.service.Location;
import com.softlayer.api.service.virtual.DedicatedHost;

import java.util.List;

/**
 * Get all available routers that can be used to order a Dedicated Host.
 *
 * This example shows how to build an skeleton of get a list of SoftLayer_Virtual_DedicatedHost
 * and pass it to SoftLayer_Virtual_DedicatedHost::getAvailableRouters method to get a list of
 * available backend routers to order Dedicated Hosts.
 *
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_DedicatedHost/getAvailableRouters
 * http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost
 * http://sldn.softlayer.com/reference/datatypes/Softlayer_Hardware
 *
 * @license <http://sldn.softlayer.com/article/License>
 * @author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * @version 1.0
 */
public class GetAvailableRouters {

    public static void main(String args[]){
        // Declare username and api key
        String username = "set me";
        String apiKey = "set me";

        // Use the method SoftLayer_Location::getDatacenters in order to get location ids.
        Location location = new Location();
        location.setId(449600L);

        // Skeleton of the dedicated host to specify the data center and configuration sizes
        // 56 Cores X 242 RAM X 1.2 TB
        DedicatedHost template = new DedicatedHost();
        template.setCpuCount(56L);
        template.setDiskCapacity(1200L);
        template.setMemoryCapacity(242L);
        template.setDatacenter(location);

        // Get Api Client and service
        ApiClient client = new RestApiClient().withCredentials(username, apiKey);
        DedicatedHost.Service service = DedicatedHost.service(client);

        try{
            // Get list of available routers by calling to getAvailableRouters method.
            List<Hardware> routers = service.getAvailableRouters(template);

            // Print response in JSON format
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(routers));

        } catch (Exception e)
        {
            System.out.println("Unable to get the backend routers: " + e);
        }
    }
}
```
