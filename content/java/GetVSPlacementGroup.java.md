---
title: "GetVSPlacementGroup.java"
description: "Retrieve the placement group that a virtual guest belongs to."
date: "2018-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "PlacementGroup"
---

```
package com.softlayer.api.test;

/*
 Get PlacementGroup

 Retrieve the placement group that a virtual guest belongs to.

 Important manual pages:
 https://softlayer.github.io/reference/services/SoftLayer_Product_Order/placeOrder/

 License: http://sldn.softlayer.com/article/License
 Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 */

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.softlayer.api.ApiClient;
import com.softlayer.api.RestApiClient;
import com.softlayer.api.service.virtual.Guest;
import com.softlayer.api.service.virtual.PlacementGroup;

public class GetVSPlacementGroup {
    public static void main(String[] arg) {
        String username = "set me";
        String apiKey = "set me";

        ApiClient client = new RestApiClient().withCredentials(username, apiKey).withLoggingEnabled();
        Guest.Service service = Guest.service(client, 11111L);

        try {

            PlacementGroup result = service.getPlacementGroup();
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(result));
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
```
